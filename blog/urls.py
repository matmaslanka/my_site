from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.posts, name='posts'),
    path('<int:post>', views.post_content_by_number),
    path('<str:post>', views.post_content,name='post-content')
]