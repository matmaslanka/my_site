from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

all_posts = {
    'post1': 'Praca w django to czysta przyjemność!',
    'post2': 'Wspinaczka to świetna rzecz!',
    'post3': None
}


def index(request):
    list_items = ''
    posts = list(all_posts.keys())

    return render(request, "blog/index.html", {
        'posts': posts
    })


def post_content_by_number(requst, post):
    posts = list(all_posts.keys())

    if post > len(posts):
        return HttpResponseNotFound('Invalid post number')

    redirect_post = posts[post - 1]
    redirect_path = reverse('post-content', args=[redirect_post])
    return HttpResponseRedirect(redirect_path)


def post_content(request, post):
    try:
        post_text = all_posts[post]
        return render(request, "blog/post.html", {
            'post_name': post,
            'text': post_text
        })
    except:
        raise Http404()
