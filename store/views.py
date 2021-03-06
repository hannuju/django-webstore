from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.cache import cache
from django.db.models import Q
from store.models import Item
from store.cart import Cart

class IndexView(ListView):
    model = Item
    template_name = 'store/index.html'

    # Passes user's last search keyword to template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        if query is None:
            query = ""
        context['lastquery'] = query
        return context

    # Initializes session by calling session.save() if it doesn't exists
    # Does SQL-query "Like" for item id and title by user's input to the search field
    # Orders by chosen radio button, default ordering by id if not chosen
    def get_queryset(self):
        if not self.request.session.session_key:
            self.request.session.save()
        query = self.request.GET.get('q') # Search input by user
        ordering = self.request.GET.get('qq') # Radio button choice for ordering
        if ordering is None:
            ordering = "id"
        if query:
            return Item.objects.filter(Q(id__icontains=query) | Q(title__icontains=query)).order_by(ordering)
        else:
            return Item.objects.order_by(ordering)

class DetailView(DetailView):
    model = Item

class ItemCreate(CreateView):
    model = Item
    fields = ['title', 'description', 'price']

class ItemUpdate(UpdateView):
    model = Item
    fields = ['title', 'description', 'price']

class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy('store:index')

# Renders cart view with user's cart if it exists
# User's cart is searched in the database cache with session key
def CartView(request):
    key = request.session.session_key
    context = {}
    if not cache.get(key) is None:
        context = {'obj' : cache.get(key)}
    return render(request, 'store/cart.html', context = context)

# AJAX call
# Creates cart for user if it doesn't exist, then adds item to user's cart
# User's cart is searched in the database cache with session key
# Refreshes cart's expiration time and sets it to 10 minutes
def addToCart(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    key = request.session.session_key
    if cache.get(key) is None:
        cache.set(key, Cart())
    userCart = cache.get(key)
    userCart.add_item(item)
    cache.set(key, userCart, 600)
    return HttpResponse(item.title)

# Deletes item from user's cart
# User's cart is searched in the database cache with session key
# Refreshes cart's expiration time and sets it to 10 minutes
def deleteFromCart(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    key = request.session.session_key
    userCart = cache.get(key)
    userCart.delete_item(item)
    cache.set(key, userCart, 600)
    return HttpResponseRedirect('/store/cart')
