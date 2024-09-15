from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, image_view, series_view, artwork_view, page_view, ImageViewSet
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register(r'images', ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("", index, name="index"),
    path("page/<slug:page_slug>", page_view),
    path("artwork/", artwork_view, name="artwork"),
    path("series/<slug:series_slug>", series_view),  # new
    path("series/<slug:series_slug>/image/<slug:image_slug>", image_view),  # new
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
