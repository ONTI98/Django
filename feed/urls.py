from django.urls import path
from .views import HomeView
from .views import PostDetailView

app_name='feed'   

urlpatterns=[
    path('',HomeView.as_view(),name='index'),
    path('post/<int:pk>',PostDetailView.as_view(),name='post_details')     
    ] 