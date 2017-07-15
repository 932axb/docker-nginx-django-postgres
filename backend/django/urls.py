from django.conf.urls import include, url
from django.contrib import admin



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^api/', include('apps.tasks.urls')),
    url(r'^', include('apps.main.urls')),
    url(r'^books/', include('apps.book.urls')),

    # url(r'^', include(router.urls)),

]
