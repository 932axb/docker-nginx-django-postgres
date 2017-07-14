# stdlib #

# core django #
from django.conf.urls import url, include

# third-party app #

# project app #
from .views import MainView

urlpatterns = [
    url(r'^$', view=MainView.as_view(), name='main-main'),
]
