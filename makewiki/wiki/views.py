from django.shortcuts import render
from wiki.models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PageList(ListView):
    """Renders all pages for the wiki."""
    model = Page

    def get(self, request):
        """ Returns a list of wiki pages. """
        pages = self.get_queryset().all()
        return render(request, "wiki/list.html", {"pages": pages})


class PageDetailView(DetailView):
    """Renders a page."""
    model = Page

    def get(self, request, slug):
        """ Returns a specific of wiki page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, "wiki/page.html", {"page": page})
