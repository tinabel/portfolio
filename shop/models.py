from django.db import models
from django.contrib.auth.models import User
from gallery.models import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from portfolio import settings
import stripe
import logging

logger = logging.getLogger(__name__)

stripe.api_key = settings.STRIPE_API_KEY

class CustomerProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    stripe_customer_id = models.CharField(max_length=120)

    # Add additional fields you want to add to the customer profile


@receiver(post_save, sender=User)
def _on_update_user(sender, instance, created, **kwargs):
  logger.debug('Just saved %s', str(instance))
  logger.debug('instance id is %s', instance.id)
  logger.debug('instance is %s', instance)

  if created:
    customer = stripe.Customer.create(
      email=instance.email,
      name=instance.get_full_name(),
      metadata={
        'user_id': instance.pk,
        'username': instance.username
      },
      description='Created from Django',
    )

    # Create profile
    profile = CustomerProfile.objects.create(user=instance, stripe_customer_id=customer.stripe_customer_id)
    profile.save()

  else:
    customer = CustomerProfile.objects.filter(user_id=instance.pk).first()
    logger.debug('customer is %s', customer)

    stripe.Customer.modify(
      customer.stripe_customer_id,
      name=instance.get_full_name(),
      email=instance.email,
      metadata={
        'user_id': instance.pk,
        'username': instance.username
      },
    )

class Product(models.Model):
  image = models.OneToOneField(
    Image,
    on_delete=models.CASCADE,
    primary_key=True,
  )
  title = models.CharField(max_length=120)
  stripe_product_id = models.CharField(max_length=120)
  price = models.DecimalField(max_digits=15, decimal_places=2, default=00.00)

@receiver(post_save, sender=Image)
def _on_update_image(sender, instance, created, **kwargs):
  logger.debug('Just saved %s', str(instance))
  logger.debug('instance id is %s', instance.id)
  logger.debug('instance is %s', instance)

  dimensions = f"{instance.print_size_width}x{instance.print_size_height}"
  description = f"Print size (in inches): {dimensions} \n {instance.alt}"

  if created:
    product = stripe.Product.create(
      price=instance.price,
      name=instance.title,
      default_price_data={
        'unit_amount_decimal': str(instance.price),
        'currency': 'usd',
      },
      description=description,
      images=[instance.image_file.url],
      shippable=True,
      type='good',
      metadata={
        'user_id': instance.pk,
        'username': instance.username
      },
      url=f"{settings.STRIPE_BASE_URL}/series/{instance.series.slug}/image/{instance.slug}",
    )

    # Create profile
    product = Product.objects.create(image=instance, stripe_product_id=product.stripe_product_id)
    product.save()

  else:
    product = Product.objects.filter(image_id=instance.pk).first()
    logger.debug('product is %s', product)

    stripe.Product.update(
      product.stripe_product_id,
      price=instance.price,
      name=instance.title,
      default_price_data={
        'unit_amount_decimal': str(instance.price),
        'currency': 'usd',
      },
      description=description,
      images=[instance.image_file.url],
      shippable=True,
      type='good',
      metadata={
        'user_id': instance.pk,
        'username': instance.username
      },
      url=f"{settings.STRIPE_BASE_URL}/series/{instance.series.slug}/image/{instance.slug}"
    )
