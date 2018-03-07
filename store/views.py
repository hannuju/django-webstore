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
    # SQL-query "Like" by user's input to the search field
    # Order by chosen radio button, default ordering by id if not chosen
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

# Renders cart view with user's cart object if it exists in database cache
def CartView(request):
    key = request.session.session_key
    context = {}
    if not cache.get(key) is None:
        context = {'obj' : cache.get(key)}
    return render(request, 'store/cart.html', context = context)

# AJAX call
# Creates cart if it doesn't exist in database cache, then adds item to cart
# Refreshes cart's expiration timer, 10 minutes till expiration
def addToCart(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    key = request.session.session_key
    if cache.get(key) is None:
        cache.set(key, Cart())
    userCart = cache.get(key)
    userCart.add_item(item)
    cache.set(key, userCart, 600)
    return HttpResponse("Yeees!")

def deleteFromCart(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    key = request.session.session_key
    if cache.get(key) is None:
        print("only possible by typing url")
    userCart = cache.get(key)
    userCart.delete_item(item)
    cache.set(key, userCart, 600)
    #context = {'obj' : cache.get(key)}
    return HttpResponseRedirect('/store/cart')
    #return render(request, 'store/cart.html', context = context)
