from django.urls import path

from . import views

app_name = 'store'
urlpatterns = [
    path('', views.IndexView.as_view()),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('add_item', views.AddItemView.as_view())

]
