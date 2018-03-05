from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from django.db.models import Q
from store.models import Item
from store.cart import Cart

class IndexView(ListView):
    model = Item
    template_name = 'store/index.html'

    def get_queryset(self):
        # Search with SQL-query "Like"
        query = self.request.GET.get('q')
        if query:
            return Item.objects.filter(Q(id__icontains=query) | Q(title__icontains=query))
        else:
            return Item.objects.all()

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
    context = {}
    print(request.session.session_key)
    # Add cart to context if it exists
    if request.session.session_key in Cart.carts:
        context = {'obj' : Cart.carts[request.session.session_key]}
    return render(request, 'store/cart.html', context = context)

# AJAX call
def addToCart(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    # Create cart if it doesn't exist, then add item to cart
    if not request.session.session_key in Cart.carts:
        Cart.carts[request.session.session_key] = Cart()
    Cart.carts[request.session.session_key].add_item(item)
    return HttpResponse("Yeees!")
