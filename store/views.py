from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from django.db.models import Q
from store.models import Item
from store.cart import Cart

print('Adding hardcoded values in dictionary')
carts = {'avain': 'arvo'}
carts['456'] = Cart()
item = get_object_or_404(Item, pk=26)
carts['456'].add_item(item)
print('Hardcoded values added')
print(carts)

def addItemToCart(item):
    print("Cart adding was called")
    key = "123"
    if not key in carts:
        carts[key] = Cart()
    carts[key].add_item(item)
    print(carts)


class IndexView(ListView):
    model = Item
    template_name = 'store/index.html'

    def get_queryset(self):
        print(carts)
        #if not self.request.session.session_key:
        #    self.request.session.save()

        # Search with SQL-query "Like"
        query = self.request.GET.get('q')
        #print(query)
        #queryy = self.request.GET.get('qq')
        #print(queryy)
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
    #key = request.session.session_key
    key = "123"
    print(len(carts))
    #print(key)
    if key in carts.keys():
        print("[INFO] Cart found!")
        context = {'obj' : carts[key]}
    else:
        print("[INFO] Cart NOT found!")
        context = {}

    return render(request, 'store/cart.html', context = context)

# AJAX call
def addToCart(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    addItemToCart(item)
    # Create cart if it doesn't exist, then add item to cart
    #key = request.session.session_key
    #key = "123"
    #if not key in carts:
    #    carts[key] = Cart()
    #carts[key].add_item(item)
    return HttpResponse("Yeees!")
