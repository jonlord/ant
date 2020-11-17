from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='order_index'),
    path('<str:client>/place', views.place, name='order_place'),
    path('<str:client>/cancel', views.place, name='order_cancel'),
    path('<str:client>/returns', views.place, name='order_returns'),
    path('<str:client>/fulfill', views.place, name='order_fulfill'),
]