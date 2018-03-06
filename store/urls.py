from django.urls import path

from . import views
from store.views import ItemCreate, ItemUpdate, ItemDelete

app_name = 'store'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('cart', views.CartView, name='cart'),
    path('item/<int:item_id>/add_to_cart', views.addToCart),
    path('item/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('item/add/', ItemCreate.as_view(), name='item-add'),
    path('item/<int:pk>/update', ItemUpdate.as_view(), name='item-update'),
    path('item/<int:pk>/delete/', ItemDelete.as_view(), name='item-delete'),
]
