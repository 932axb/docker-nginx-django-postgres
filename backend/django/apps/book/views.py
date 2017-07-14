# stdlib #
import logging

# core django #
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.list import View

# third-party app #

# project app #

#logger = logging.getLogger(__name__)


class BookView(View):
    def get(self, request):
        return render_to_response('book/book_main.html', locals(), RequestContext(request))