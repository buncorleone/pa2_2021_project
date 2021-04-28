from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
    name = models.CharField(max_length=50)
    hashtag = models.CharField(max_length=20)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    @property
    def as_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "hashtag": f"{self.hashtag}",
            "created": f"{self.created}",
            "updated": f"{self.updated}"
        }

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        verbose_name_plural = "Posts"
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    @property
    def as_dict(self):
        return {
            "title": self.title,
            "body": self.body,
            "category": f"{self.category}",
            "author": f"{self.author}"
        }

    def __str__(self):
        return self.title
