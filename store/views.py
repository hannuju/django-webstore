from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.db.models import Q
from store.models import Item

class IndexView(ListView):
    model = Item
    template_name = 'store/index.html'

    def get_queryset(self):
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
