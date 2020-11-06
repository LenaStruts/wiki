from django.shortcuts import render

from . import util


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
            "entry": markdowner.convert(entry_page),
            "entry_title": title
        })
