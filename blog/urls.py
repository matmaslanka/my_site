from django.urls import path

from . import views

urlpatterns = [
    path('', views.StartPageView.as_view(), name='index'),
    # path('', views.index, name='index'),
    path('posts', views.AllPostsView.as_view(), name='posts'),
    # path('posts', views.posts, name='posts'),
    # path('<int:post>', views.post_content_by_number),
    # path('<str:post>', views.post_content,name='post-content'),
    path('posts/<slug:slug>', views.SinglePostView.as_view(), name='post-content'),
    # path('posts/<slug:slug>', views.post_content,
    #      name='post-content')  # posts/my-first-post
    path('read-later', views.ReadLaterView.as_view(), name='read-later'),
]
