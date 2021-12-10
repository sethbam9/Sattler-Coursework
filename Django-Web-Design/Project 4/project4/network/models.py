from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm
from django import forms


class User(AbstractUser):
    following = models.ManyToManyField('User', symmetrical=False, related_name='followers')
    likes = models.ManyToManyField('Post', related_name='likers')

class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    post = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class PostForm(ModelForm):
    post = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Type here...'}), label='')

    class Meta:
        model = Post
        exclude = ('creator', 'timestamp')
