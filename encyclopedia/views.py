from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import NewEntry

from . import util

import secrets

from markdown2 import Markdown

markdowner = Markdown()
   
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    entry_page = util.get_entry(title)
    if entry_page is None:
        return render(request, "encyclopedia/non.html", {
            "entry_title": title    
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry_title": title,
            "entry": markdowner.convert(entry_page)
        })


def add(request):
    entry_exists = False
    if request.method == "POST":
        form = NewEntry(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if util.get_entry(title) is None:
                util.save_entry(title, content)
            else:
                entry_exists = True
    return render(request, "encyclopedia/add.html", {
        "form": NewEntry(),
        "entry_exists": entry_exists
    })


def edit(request, title):
    if request.method == "POST":
        form=NewEntry(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return render(request, "encyclopedia/entry.html", {
            "entry": markdowner.convert(content),
            "entry_title": title
        })
    else:
        entry_page = util.get_entry(title)
        form=NewEntry(initial={'title': title, 'content': entry_page})
        return render(request, "encyclopedia/edit.html", {'form': form})


def search(request):
    found = False
    value = request.GET.get('q')
    entries = util.list_entries()
    if(util.get_entry(value) is not None):
        found = True
        return render(request, "encyclopedia/entry.html", {
            "entry": markdowner.convert(util.get_entry(value)),
            "entry_title": value
        })
    else:
        filtered_entries = []
        for entry in util.list_entries():
            if value.lower() in entry.lower():
                filtered_entries.append(entry)
                found = True
        return render(request, "encyclopedia/search_results.html", {
            "filtered_entries": filtered_entries,
            "entry": entry,
            "found": found
        })


def random(request):
    entries = util.list_entries()
    random_entry = secrets.choice(entries)
    return HttpResponseRedirect(reverse("entry", kwargs={'title': random_entry}))

