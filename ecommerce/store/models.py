from django.db import models
from django.urls import reverse


class Status(models.TextChoices):
    ACTIVE = 'Active', 'Active'
    MODIFIED = 'Modified', 'Modified'
    PASSIVE = 'Passive', 'Passive'


class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)
    status = models.CharField(max_length=10,
                              choices=Status.choices,
                              default=Status.ACTIVE)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list-category', args=[self.slug])


class Product(models.Model):
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default='un-brand')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=10,
                              choices=Status.choices,
                              default=Status.ACTIVE)
    # pip install Pillow
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category,
                                 related_name='product',
                                 on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product-info', args=[self.slug])
