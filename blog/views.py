from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

all_posts = {
    'post1': 'Praca w django to czysta przyjemność!',
}


def index(request):
    return HttpResponse("Its ok!")


def post_content_by_number(requst, post):
    posts = list(all_posts.keys())

    if post > len(posts):
        return HttpResponseNotFound('Invalid month')
    
    redirect_post = posts[post - 1]
    redirect_path = reverse('post-content', args=[redirect_post])
    return HttpResponseRedirect(redirect_path)


def post_content(request, post):
    try:
        post_text = all_posts[post]
    except:
        raise Http404()
    return HttpResponse(post_text)
