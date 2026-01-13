from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio_page, name='portfolio'),
    path('profile/', views.profile, name='profile'),
    path('profile2/', views.profile2, name='profile2'),
    path('roadmap/', views.profile3, name='roadmap'),
]

