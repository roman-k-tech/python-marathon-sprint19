from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/v1/book', views.BookView)

urlpatterns = \
    [
        path('', views.books, name='books'),
        path('books/', views.books, name='books'),
        path('books/<int:book_id>/', views.book_item, name='book_item'),
        path('books/create/', views.create_book, name='create_book'),
        path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
        path('books/update/<int:pk>/', views.update_book, name='update_book'),
        path('', include(router.urls))
    ]
