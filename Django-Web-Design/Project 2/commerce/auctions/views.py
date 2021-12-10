from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *

import operator
import decimal
import datetime

# Active listings page
def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.filter(is_active=True)
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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))

    else:
        form = ListingForm()

    return render(request, "auctions/create.html", {
        "form": form
    })


def listing(request, listing_id):

    listing = Listing.objects.get(id=listing_id)

    if request.method == 'POST':
        new_bid = decimal.Decimal(request.POST["bid"])
        watching = request.POST.get("watchlist")
        closed = request.POST.get("close")
        comment_body = request.POST.get("comment")

        if watching:
            user_listing = UserListing(watcher=request.user, listing=listing)
            user_listing.save()

        bids = Bid.objects.filter(listing=listing)

        if listing.starting_bid > new_bid:
            return HttpResponse("Too low")

        if len(bids) >= 1:
            for bid in bids:
                if bid.amount > new_bid:
                    return HttpResponseRedirect("Too low")

            new_price = Bid.objects.create(listing=listing, bidder=request.user, amount=new_bid)
            new_price.save()
            return HttpResponseRedirect(reverse("index"))

        if not comment_body == "":
            new_comment = Comment.objects.create(commenter=request.user, listing=listing, body=comment_body, created_on=datetime.datetime.now())

    return render(request, "auctions/listing.html", {
        "listing": listing,
        "comments": Comment.objects.filter(listing=listing)
    })

@login_required
def watchlist(request):
    return render(request, "auctions/watchlist.html", {
        "user_listings": UserListing.objects.filter(watcher=request.user)
    })


def categories(request):
    l = Listing.objects.all()
    c = Category.objects.all()
    for i in l:
        print(f"category is {i.id}")
    for i in c:
        print(f"category ID is {i.id}")
    return render(request, "auctions/categories.html", {
        "categories": Category.objects.order_by('name')
    })


def category(request, category_id):
    category = Category.objects.get(id=category_id)
    print(category.name)
    return render(request, "auctions/category.html", {
        "listings": Listing.objects.all(),
        "category": category
    })
