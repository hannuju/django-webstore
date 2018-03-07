from django.urls import path

from . import views
from store.views import ItemCreate, ItemUpdate, ItemDelete

app_name = 'store'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('cart', views.CartView, name='cart'),
    path('item/<int:item_id>/add_to_cart', views.addToCart, name='add-to-cart'),
    path('cart/<int:item_id>/delete_from_cart', views.deleteFromCart, name='delete-from-cart'),
    path('item/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('item/create/', ItemCreate.as_view(), name='item-create'),
    path('item/<int:pk>/update', ItemUpdate.as_view(), name='item-update'),
    path('item/<int:pk>/delete/', ItemDelete.as_view(), name='item-delete'),
]
