from distutils.command.upload import upload
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    text = models.CharField(max_length=255)
    created_time = models.TimeField(auto_now_add=True)
    created_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Media(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_medias")
    image = models.ImageField(upload_to="images")
    video = models.FileField(upload_to="videos")
    video_thumbnail = models.FileField(upload_to="videos_thumbnail")
    created_time = models.TimeField(auto_now_add=True)
    created_date = models.DateField(auto_now_add=True)


class StatusEnum(models.IntegerChoices):
    ONE = 1, 'Like'
    TWO = 2, 'Heart'
    THREE = 3, 'Angry'
    FOUR = 4, 'Haha'


class Like(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_likes")
    reaction_type = models.SmallIntegerField(
        choices=StatusEnum.choices, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_comments")
    text = models.CharField(max_length=255)
    media = models.FileField(upload_to="comment")
    created_time = models.TimeField(auto_now_add=True)
    created_date = models.DateField(auto_now_add=True)
