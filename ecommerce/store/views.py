from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def store(request):
    all_products = Product.objects.all()

    data = {
        'all_products': all_products
    }

    return render(request,
                  template_name='store/store.html',
                  context=data)


def categories(request):
    all_categories = Category.objects.all()

    return {
        'all_categories': all_categories
    }


# http://127.0.0.1:8000/boxing-gloves/create
def list_category(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)

    products = Product.objects.filter(category=category)
    # yukardaki django query'sinin aşağıda TSQL karşılığıdır
    # select * from Products where category=category

    return render(request,
                  'store/list-category.html',
                  {
                      'category': category,
                      'products': products
                  })


def product_info(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)

    context = {
        'product': product
    }

    return render(request,
                  'store/product-info.html',
                  context)
