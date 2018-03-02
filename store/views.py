
from django.views import generic

from store.forms import AddItemForm
from .models import Item

class IndexView(generic.ListView):
    model = Item
    template_name = 'store/index.html'

class DetailView(generic.DetailView):
    model = Item
    template_name = 'store/detail.html'

class AddItemView(generic.FormView):
    template_name = 'store/add_item.html'
    form_class = AddItemForm
    success_url = '/store/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
