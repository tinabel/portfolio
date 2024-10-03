from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from rest_framework import viewsets
from .models import Image, Series, Page, Cart, CartItem
from .serializers import ImageSerializer
from .forms import ContactForm

def index(request):
  images = Image.objects.filter(is_featured=True)
  series = Series.objects.filter(is_featured=True).order_by('position')
  featured_series_image_ids = series.all().values_list('cover_image', flat = True)
  series_images = Image.objects.filter(id__in=featured_series_image_ids).order_by('series__position')

  return render(request, 'index.html', {'featured_images': images, 'featured_series': series, 'featured_series_images': series_images})

def artwork_view(request):
  all_series = Series.objects.all().order_by('position')
  series_image_ids = all_series.values_list('cover_image', flat = True)
  series_images = Image.objects.filter(id__in=series_image_ids).order_by('series__position')
  return render(request, 'artwork.html', {'series': all_series, 'series_images': series_images})

def series_view(request, series_slug):
  series = Series.objects.get(slug=series_slug)
  images = Image.objects.filter(series_id=series.id)
  return render(request, 'series.html', { 'series': series, 'series_images': images })

def image_view(request, series_slug, image_slug):
  image = Image.objects.get(slug=image_slug)
  return render(request, 'image.html', {'image': image, 'image_slug': image_slug })

def page_view(request, page_slug):
  content = Page.objects.get(slug=page_slug)
  return render(request, 'page.html', {'page_slug': page_slug, 'page_content': content })

def contact(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      pass
      return redirect('success')
  else:
    form = ContactForm()
  return render(request, 'contact.html', {'form': form})

def success(request):
  return HttpResponse('Your message was successfully sent. Thank you!')

class ImageViewSet(viewsets.ModelViewSet):
  queryset = Image.objects.all()
  serializer_class = ImageSerializer
  template_name = 'image.html'

def add_to_cart(request, image_id):
  product = get_object_or_404(Image, id=image_id)
  cart_id = request.session.get('cart_id')
  if not cart_id:
    cart = Cart.objects.create()
    request.session['cart_id'] = cart.id
  else:
    cart = get_object_or_404(Cart, id=cart_id)

  cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
  if not created:
    cart_item.quantity += 1
  cart_item.save()

  return redirect('cart_detail')

def update_cart_item(request, item_id):
  cart_item = get_object_or_404(CartItem, id=item_id)
  if request.method == 'POST':
    cart_item.quantity = int(request.POST.get('quantity', 1))
    cart_item.save()
  return redirect('cart_detail')

def cart_detail(request):
  cart_id = request.session.get('cart_id')
  if not cart_id:
    return render(request, 'cart_detail.html', {'cart': None, 'total_price': 0})

  cart = get_object_or_404(Cart, id=cart_id)
  total_price = sum(item.total_price() for item in cart.cartitem_set.all())

  return render(request, 'cart_detail.html', {'cart': cart, 'total_price': total_price})

def remove_from_cart(request, product_id):
  cart_id = request.session.get('cart_id')
  cart = get_object_or_404(Cart, id=cart_id)
  cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
  cart_item.delete()
  return redirect('cart_detail')
