# stdlib #
import logging

# core django #
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.list import View
from django.shortcuts import render, get_object_or_404

# third-party app #

# project app #
from .models import Book

#logger = logging.getLogger(__name__)


class ListBookView(View):
    def get(self, request):
        books = Book.published.all()
        return render_to_response('book/book_list.html', locals(), RequestContext(request))


class DetailBookView(View):
    def get(self, request, book_slug):
        book = get_object_or_404(
            Book,
            slug=book_slug
        )
        return render_to_response('book/book_detail.html', locals(), RequestContext(request))