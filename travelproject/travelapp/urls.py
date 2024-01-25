from django.urls import path

from . import views
app_name="travelapp"
urlpatterns = [
    path('', views.demo, name='demo'),
    path('about/', views.about, name='about'),
]