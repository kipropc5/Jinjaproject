from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='my_index'),
    path('about/', views.about, name='my_about'),
    path('contact/', views.contact, name='my_contact'),
    path('base/', views.base, name='my_base'),

]
