'''Define URL patterns for users'''

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
               # Default auth urls - login
               path('', include('django.contrib.auth.urls')),
               # Registration page
               path('register/', views.register, name='register'),
]