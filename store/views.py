from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.cache import cache

from django.db.models import Q
from store.models import Item
from store.cart import Cart

class IndexView(ListView):
    model = Item
    template_name = 'store/index.html'

    def get_queryset(self):
        # Save the session key first time opening the index page
        if not self.request.session.session_key:
            self.request.session.save()

        # Search with SQL-query "Like"
        query = self.request.GET.get('q')
        if query:
            return Item.objects.filter(Q(id__icontains=query) | Q(title__icontains=query)).order_by('-price')
        else:
            return Item.objects.all()
            #return Item.objects.order_by('title')

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
    success_url = reverse_lazy('item-list')

def CartView(request):
    # Add cart to context if it exists
    key = request.session.session_key
    print(key)
    if not cache.get(key) is None:
        print("[INFO] Cart found!")
        context = {'obj' : cache.get(key)}
    else:
        print("[INFO] Cart NOT found!")
        context = {}
    return render(request, 'store/cart.html', context = context)

# AJAX call
def addToCart(request, item_id):
    key = request.session.session_key
    print(key)
    item = get_object_or_404(Item, pk=item_id)
    # Create cart if it doesn't exist, then add item to cart
    if cache.get(key) is None:
        cache.set(key, Cart())
    userCart = cache.get(key)
    userCart.add_item(item)
    cache.set(key, userCart, 600) # expire timer = 10 min
    return HttpResponse("Yeees!")
