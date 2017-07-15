# stdlib #

# core django #
from django.conf.urls import url, include

# third-party app #

# project app #
from .views import ListBookView, DetailBookView

urlpatterns = [
    url(r'^$', view=ListBookView.as_view(), name='book-list'),
    url(r'^detail/(?P<book_slug>[-\w]+)/$', view=DetailBookView.as_view(), name='book-detail'),
]
