from django.urls import path
from .views import HomeView

app_name='feed'

urlpatterns=[
    path('',HomeView.as_view(),name='index'),
    
]  