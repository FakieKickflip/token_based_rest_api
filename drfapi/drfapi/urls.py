
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from drf_app import views

from rest_framework.authtoken import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('generate_a_token/', auth_views.obtain_auth_token, name="generate_a_token"), #path to generate a token for username and password.
    
    path('get_articles/', views.get_articles, name='get_articles'),
    path('one_article/<int:pk>/', views.one_article, name='one_article'),
    path('create_article/', views.create_article, name='create_article'),

    path('get_authors/', views.get_authors, name='get_author'),
    path('one_author/<int:pk>/', views.one_author, name='one_author'),
    path('create_author/', views.create_author, name='create_author'),
]


urlpatterns = format_suffix_patterns(urlpatterns)