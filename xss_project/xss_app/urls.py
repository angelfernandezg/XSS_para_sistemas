from django.urls import path
from . import views

urlpatterns = [
    path('vulnerable/', views.xss_vulnerable, name='xss_vulnerable'),
    path('protected/', views.xss_protected, name='xss_protected'),
]

