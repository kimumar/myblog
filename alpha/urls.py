from django.conf.urls import url
from django.urls import path
from.import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blog_details/<int:pk>/', views.blogs, name='blog_details'),
    path('contact', views.contact, name='contact'),
    path('create', views.create, name='create'),
]