from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('domains/', views.domains, name='domains'),
    path('domains/<int:domain_id>', views.domain, name='domain'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
    path('contact_us/', views.contact_us, name='contacts'),
]