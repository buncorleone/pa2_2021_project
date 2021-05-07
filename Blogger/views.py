from django.contrib.auth import get_user_model
# Temporary HttpResponse import used for testing, to be removed once GUI is done and views point to that.
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from . import models
from . import serializers
import json


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


class Posts(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        posts = models.Post.objects.all()

        returning_json = {"posts": []}
        for post in posts:
            returning_json["posts"].append(post.as_dict)

        return JsonResponse(returning_json, status=200)

    def post(self, request):
        content = request.data
        author = request.user
        models.Post.objects.create(
            author=author,
            title=content['title'],
            category=models.Category.objects.filter(name=content["category"]).first(),
            body=content['body']
        )
        return JsonResponse(content, status=200)


# def create_post(request):
#     if request.method == 'POST':
#         content = request.body
#         pst_title = content.value['title']
#         pst_cat = content.value['category']
#         pst_body = content.value['body']
#         pst_auth = get_user_model()


class Categories(APIView):
    def get(self, request):
        categories = models.Category.objects.all()

        returning_json = {"categories": []}
        for category in categories:
            returning_json["categories"].append(category.as_dict)

        return JsonResponse(returning_json, status=200)


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


# All code below was taken from wk11_drf_demo-master
class Register(APIView):
    """
    Allows a new user to register an account.
    """

    def post(self, request):
        """
        Takes the following JSON structure as input:

        {"username": "string", "password": "string", "first_name": "string", "last_name": "string", "is_admin": "boolean"}            }

        """
        try:
            if not request.data:
                raise ValueError("Invalid User data")

            # serialized_data = serializers.RegisterSerializer(data=request.data)
            # if serialized_data.is_valid(raise_exception=True):
            incoming_data = {
                "username": request.data["username"],
                "password": request.data["password"],
                "first_name": request.data["first_name"],
                "last_name": request.data["last_name"],
                "email": f"{request.data['first_name']}.{request.data['last_name']}@tudublin.ie",
                "is_staff": request.data["is_admin"],
            }
            new_user = get_user_model().objects.create_user(**incoming_data)

            return Response({
                "username": request.data["username"],
                "first_name": request.data["first_name"],
                "last_name": request.data["last_name"],
                "is_admin": request.data["is_admin"],
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)


class UserMeDetails(generics.RetrieveAPIView):
    """"
    Retrieves a summarized view of the current User object.
    """
    serializer_class = serializers.UserMeSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_object(self):
        return self.request.user
