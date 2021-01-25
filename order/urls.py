from django.urls import path, include
from . import views
from .views import *

urlpatterns = \
    [
        path('orders', views.orders, name='orders'),
        path('orders/delete/<int:order_id>/', views.delete_order),
        path('orders/form', views.orders_form, name='create_orders'),
        path('orders/form/<int:order_id>/', views.orders_form, name='update_orders'),
        path('api/v1/order/', OrderListCreate.as_view()),
        path('api/v1/order/<int:pk>/', OrderViewUpdateDelete.as_view()),
    ]
