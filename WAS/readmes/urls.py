from django.urls import path

from . import views

app_name = 'readmes'
urlpatterns = [
    path('', views.craft, name='craft'),
]