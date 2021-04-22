from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Welcome to the Blogger homepage')


def my_posts(request):
    return HttpResponse('Your posts will appear here.')


def list_posts(request):
    return HttpResponse('All posts will be listed here.')


def list_categories(request):
    return HttpResponse('All categories will be listed here. Admins will be allowed to change them.')
