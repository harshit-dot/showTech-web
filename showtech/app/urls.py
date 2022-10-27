from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.main, name='main'),
    path('result', views.result, name='result'),
]