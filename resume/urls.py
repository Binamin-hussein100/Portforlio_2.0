from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.works,name='work'),
    path('projects/',views.projo,name='projects')
]
