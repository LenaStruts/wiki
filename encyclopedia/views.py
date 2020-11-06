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
