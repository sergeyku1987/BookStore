from django.contrib import admin
from django.urls import include, path
from base import settings

from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
]


if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls"))
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
