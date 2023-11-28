
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.book_form),
    path('list/',views.book_list,name='book_list')
]