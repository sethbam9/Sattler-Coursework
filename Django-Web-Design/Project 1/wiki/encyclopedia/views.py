from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django import forms
import markdown2
import random
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request, title):
    if not util.get_entry(title):
        return HttpResponseNotFound("ERROR! This page does not exist.")

    entry = util.get_entry(title)
    return render(request, "encyclopedia/entry.html", {
        'content': markdown2.markdown(entry),
        'title': title,
    })

def search_results(request):

    if request.method == "GET":
        query = request.GET.get('q')

        if query in util.list_entries():
            return entry_page(request, query)

        else:
            return render(request, "encyclopedia/results.html", {
                'entries': util.list_entries(),
                'query': query
            })

def create_entry(request):
    return render(request, "encyclopedia/create.html")

def save_entry(request):

    if request.method == "GET":
        title = request.GET.get('title')
        content = request.GET.get('markdown')
        edit = request.GET.get('boolean')

        if title in util.list_entries() and not edit:
            return(HttpResponse("ERROR. This entry already exists."))

        elif title in util.list_entries():
            util.save_entry(title, bytes(content, 'utf8'))
            return entry_page(request, title)

        else:
            util.save_entry(title, bytes(content, 'utf8'))
            return entry_page(request, title)

def edit_entry(request, title):
    return render(request, "encyclopedia/edit.html", {
        'entry': util.get_entry(title),
        'title': title,
    })

def random_entry(request):
    entry = random.choice(util.list_entries())
    return entry_page(request, entry)
