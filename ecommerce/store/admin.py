from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    # name üzerinden slug üretmek için.
    prepopulated_fields = {
        'slug': ('name', )
    }
    fields = ['name', 'slug']  # admin category eklerken hangi alanları görebilecek. status, ip_address, machine_name, create_date vb bilgilere müdahele etmesini istemiyorsak onları buraya yazmıyoruz.


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }
    fields = ['title', 'slug', 'description', 'price', 'image', 'category']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
