from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

import random

import markdown2

from . import util

# "Home" page that displays a list of all of the entries saved.
def index(request):

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Error page that displays whatever error message is passed in.
def error(request, message):
    return render(request, "encyclopedia/error.html",  {
        "message": message
    })

# Displays whatever wiki entry the user is trying to access.
def wiki(request, title):

    # If the method is POST, I update the content with the new content and then display that page.
    if request.method == "POST":
        textarea = request.POST.get('textarea')
        util.save_entry(title, bytes(textarea, 'utf8'))
    # If no entry exists with this title, display error message.
    elif util.get_entry(title) == None:
        return HttpResponseRedirect(reverse("error", kwargs={'message':"No such page exists with the specified path."}))

    # Render desired page. No conditionals necessary because I aleady have updated above and ensured that the page exists.
    return render(request, "encyclopedia/wiki.html", {
        "title": title,
        "textarea": markdown2.markdown(util.get_entry(title))
    })

# Either displays entry page for exact match or possible entries for partial matches.
def search(request):
    
    search_options = []
    if request.method == "POST":
        search = request.POST.get('q')
        
        entries = util.list_entries()

        # Redirect to page that matches search.
        if search in entries:
            return HttpResponseRedirect(reverse("wiki", kwargs={'title':search}))
        
        # Find all partial matches and add them to a list.
        for entry in entries:
            if search in entry:
                search_options.append(entry)
    
    # Display all partial matches. Displays empty page if there are none or if the user entered the url of the search page.
    return render(request, "encyclopedia/search.html", {
        "search_options": search_options
    })

# Adds new entry to saved entries.
def add(request):

    # If the method is POST, check for errors and then save the new entry.
    if request.method == "POST":
        textarea = request.POST.get('textarea')
        title = request.POST.get('title')

        # Display error message if there are duplicates or no title was entered.
        if title in util.list_entries():
            return HttpResponseRedirect(reverse("error", kwargs={'message':"There is already an existing entry with this title."}))
        elif not title:
            return HttpResponseRedirect(reverse("error", kwargs={'message':"You cannot create an entry with no title."}))

        util.save_entry(title, bytes(textarea, 'utf8'))

        # Redirect to new entry page.
        return HttpResponseRedirect(reverse("wiki", kwargs={'title':title}))

    # Render the add page with an empty form.
    return render(request, "encyclopedia/add.html")

# Allows users to edit existing entries.
def edit(request):

    # If the method is POST, get the title from the hidden form field and prepopulate the edit form with the data.
    if request.method == "POST":
        title = request.POST.get('title')

        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "textarea": util.get_entry(title)
        })

    # Send users home if they try to access this page through a url.
    return HttpResponseRedirect(reverse("index"))

# Grabs a random entry and redirects to that page.
def random_entry(request):

    return HttpResponseRedirect(reverse("wiki", kwargs={'title':random.choice(util.list_entries())}))