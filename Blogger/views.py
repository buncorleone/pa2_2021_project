from django.contrib.auth import get_user_model
# Temporary HttpResponse import used for testing, to be removed once GUI is done and views point to that.
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
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
    if request.method == 'GET':
        posts = models.Post.objects.all()

        returning_json = {"posts": []}
        for post in posts:
            returning_json["posts"].append(post.as_dict)

        return JsonResponse(returning_json, status=200)
    if request.method == 'POST':
        content = request.body
        pst_title = content.value['title']
        pst_cat = content.value['category']
        pst_body = content.value['body']
        # pst_auth = get_user_model()
        return JsonResponse(pst_title, status=200)


# def create_post(request):
#     if request.method == 'POST':
#         content = request.body
#         pst_title = content.value['title']
#         pst_cat = content.value['category']
#         pst_body = content.value['body']
#         pst_auth = get_user_model()


def list_categories(request):
    categories = models.Category.objects.all()

    returning_json = {"categories": []}
    for category in categories:
        returning_json["categories"].append(category.as_dict)

    return JsonResponse(returning_json, status=200)

