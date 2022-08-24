from django.urls import path
from . import views


app_name = 'blog1'  # URL Reverse에서 namespace역할을 수행

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
