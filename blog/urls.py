from django.urls import path
from .import views
from django.conf import settings

urlpatterns = [
    path('',views.blog, name="blog"),
    path('category/<int:categoryId>', views.category, name='category')#indica el id de la categoria a acceder
]