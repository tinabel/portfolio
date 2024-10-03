from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import add_to_cart, cart_detail, index, image_view, remove_from_cart, series_view, artwork_view, page_view, ImageViewSet, update_cart_item
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
    path("series/<slug:series_slug>/image/<slug:image_slug>", image_view),
    path('cart/add/<int:image_id>/', add_to_cart, name='add_to_cart'),
    path('cart/update/<int:item_id>/', update_cart_item, name='update_cart_item'),
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/remove/<int:image_id>/', remove_from_cart, name='remove_from_cart'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
