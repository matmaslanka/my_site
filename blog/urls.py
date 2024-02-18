from django.urls import path

from . import views

urlpatterns = [
    path('<int:post>', views.post_content_by_number),
    path('<str:post>', views.post_content,name='post-content')
]