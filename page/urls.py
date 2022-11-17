
from django.urls import path 
from .import views
from django.conf import settings

urlpatterns = [
    path('<int:pageId>/', views.sample, name='sample')
]
