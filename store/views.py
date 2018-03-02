
from django.views import generic

from store.forms import HomeForm
from .models import Item

class IndexView(generic.ListView):
    model = Item
    template_name = 'store/index.html'

class AddItemView(generic.FormView):
    template_name = 'store/add_item.html'
    form_class = HomeForm
    success_url = '/store/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
