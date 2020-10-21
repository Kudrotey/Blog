'''Defines URL patterns for blog_app'''

from django.urls import path

from . import views

app_name = 'blog_app'
urlpatterns = [
                # Home page
                path('', views.home, name='home'),
                # Headlines
                path('headlines/', views.headlines, name='headlines'),
                # Description of each headline
                path('headlines/<int:headline_id>/', views.description, name='description'),
                # Page for adding new headlines
                path('new_headline/', views.new_headline, name='new_headline'),
                # Page for adding new descriptions
                path('new_description/<int:headline_id>/', views.new_description, name='new_description'),
                # Page for editing description
                path('edit_description/<int:description_id>', views.edit_description, name='edit_description'),
               ]