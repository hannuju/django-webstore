from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#from store.forms import SearchForm
from store.models import Item

class IndexView(ListView):
    model = Item
    template_name = 'store/index.html'

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
