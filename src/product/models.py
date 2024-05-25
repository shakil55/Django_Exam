from django.db import models
from config.g_model import TimeStampMixin


# Create your models here.
from django.db import models

class Variant(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=255)
    sku = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    variants = models.ManyToManyField(Variant, blank=True)

    def __str__(self):
        return self.title

class ProductImage(TimeStampMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file_path = models.URLField()


class ProductVariant(TimeStampMixin):
    variant_title = models.CharField(max_length=255)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ProductVariantPrice(TimeStampMixin):
    product_variant_one = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
                                            related_name='product_variant_one')
    product_variant_two = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
                                            related_name='product_variant_two')
    product_variant_three = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
                                              related_name='product_variant_three')
    price = models.FloatField()
    stock = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)