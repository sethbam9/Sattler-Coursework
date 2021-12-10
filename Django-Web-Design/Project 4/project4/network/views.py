from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator

from .models import *

# Renders 10 posts per page.
def get_page(request, posts):

    page_num = request.GET.get('page', 1) # if not found, assign 1.
    paginator = Paginator(posts, 10) # display 10 posts per page.
    page = paginator.page(page_num)

    return page


# The main page.
def index(request):

    # Get all posts
    posts = Post.objects.order_by("-timestamp").all()

    return render(request, "network/index.html", {
        'page': get_page(request, posts)
    })


# Function that is called when "New Post" button is clicked at the index page.
@login_required
def create(request):
    # Code implementation from staff solution to commerce.
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.creator = request.user #The user assigned as the post's creator.
            post.save()
            # Return to the index if the form was a success.
            return HttpResponseRedirect(reverse("index"))

        # Refresh page if the form is not valid.
        else:
            return render(request, "network/create.html", {
                "form": form
            })
    else:
        return render(request, "network/create.html", {
            "form": PostForm()
        })


# Page with an individual's profile.
def profile(request, username):
    # Collect all of the user's posts in reverse chronological order (newest first)
    posts = Post.objects.order_by("-timestamp").filter(creator__username=username)
    profile = User.objects.get(username=username)

    follow = False # boolean to determine whether "follow" or "unfollow" should display.
    button = "Follow" # follow btn content.

    # If the follows this profile, display the "Unfollow" btn.
    if request.user in profile.followers.all():
        follow = True
        button = "Unfollow"

    return render(request, "network/profile.html", {
        'page': get_page(request, posts),
        'profile': profile,
        'following': profile.following.count(),
        'followers': profile.followers.count(),
        'follow': follow,
        'button': button
    })


# Display all of the posts for users that the current user follows.
@login_required
def following(request):
    # Get all posts
    following = request.user.following.all()
    posts = Post.objects.order_by("-timestamp").filter(creator__in=following)
    
    return render(request, "network/following.html", {
        'page': get_page(request, posts)
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
