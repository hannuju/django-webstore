from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.cache import cache

from django.db.models import Q
from store.models import Item
from store.cart import Cart

def addItemToCart(item):
    print("[LOCAL CACHE] Adding item to cart.")
    if cache.get('123') is None:
        cache.set('123', Cart())

    x = cache.get('123')
    x.add_item(item)
    cache.set('123', x)


class IndexView(ListView):
    model = Item
    template_name = 'store/index.html'

    def get_queryset(self):
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
    #print(cache.get('123').cart)
    #print(len(cache.get('123').cart))
    #print(key)
    if not cache.get('123') is None:
        print("[INFO] Cart found!")
        context = {'obj' : cache.get('123')}
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
