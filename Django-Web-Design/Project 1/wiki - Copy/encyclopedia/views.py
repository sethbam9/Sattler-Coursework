from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django import forms
import markdown2
import random

from . import util


class EditEntryForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)

class CreateEntryForm(forms.Form):
    # title = forms.CharField(label="",
    #     widget=forms.TextInput(attrs={
    #         'placeholder': 'Title',
    #         'margin-bottom: 10px'
    #         }))
    content = forms.CharField(label="",
        widget=forms.Textarea(attrs={'placeholder': 'Markdown Content'}))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request, title):
    if not util.get_entry(title):
        return HttpResponse("ERROR! This page does not exist.")

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
    return render(request, "encyclopedia/create.html", {
        'form': CreateEntryForm()
    })

# def save_entry(request):
#
#     if request.method == "GET":
#         title = request.GET.get('title')
#         content = request.GET.get('markdown')
#         edit = request.GET.get('boolean')
#
#         if title in util.list_entries() and not edit:
#             return(HttpResponse("ERROR. This entry already exists."))
#
#         elif title in util.list_entries():
#             util.save_entry(title, bytes(content, 'utf8'))
#             return entry_page(request, title)
#
#         else:
#             util.save_entry(title, bytes(content, 'utf8'))
#             return entry_page(request, title)

def save_entry(request):

    if request.method == "POST":
        form = NewTaskForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            edit = form.cleaned_data['boolean']

            if title in util.list_entries() and not edit:
                return HttpResponseRedirect("ERROR. This entry already exists.")

            elif title in util.list_entries():
                util.save_entry(title, bytes(content, 'utf8'))
                return HttpResponseRedirect("ERROR. This entry already exists.")

            else:
                util.save_entry(title, bytes(content, 'utf8'))
                # return entry_page(request, title)
                return HttpResponseRedirect("ERROR. This entry already exists.")

        else:
            return render(request, 'encyclopedia/create.html', {
                "form": form
            })

    return render(request, "encyclopedia/create.html", {
        "form": NewTaskForm()})


def edit_entry(request, title):
    return render(request, "encyclopedia/edit.html", {
        'entry': util.get_entry(title),
        'title': title,
    })

# def random_entry(request):
