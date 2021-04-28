from django.contrib.auth import get_user_model
from django.shortcuts import render
# Temporary HttpResponse import used for testing, to be removed once GUI is done and views point to that.
from django.http import HttpResponse
from django.http import JsonResponse
from . import models


def index(request):
    return HttpResponse('Welcome to the Blogger homepage')


def my_posts(request):
    my_posts_list = models.Post.objects.all()

    returning_json = {"posts": []}
    for post in my_posts_list:
        current_user = get_user_model()
        while post.author == current_user:
            returning_json["posts"].append(post.as_dict)

    return JsonResponse(returning_json, status=200)


def list_posts(request):
    posts = models.Post.objects.all()

    returning_json = {"posts": []}
    for post in posts:
        returning_json["posts"].append(post.as_dict)

    return JsonResponse(returning_json, status=200)


def list_categories(request):
    categories = models.Category.objects.all()

    returning_json = {"categories": []}
    for category in categories:
        returning_json["categories"].append(category.as_dict)

    return JsonResponse(returning_json, status=200)
