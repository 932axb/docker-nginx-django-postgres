# stdlib #

# core django #
from django.conf.urls import url, include

# third-party app #

# project app #
from .views import BookView

urlpatterns = [
    url(r'^list/$', view=BookView.as_view(), name='book-main'),
]
