from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator


def index(request):
    products = Product.objects.all()
    page = request.GET.get('page')

    search_text = request.GET.get('search')

    if search_text:
        search_text.lower()

    sorted_products = []

    if search_text:
        for product in products:
            if search_text in product.name.lower() or search_text in product.category or search_text + 's' in product.category:
                sorted_products.append(product)

        paginator_for_search = Paginator(sorted_products, 2)
        paginator_sorted_products = paginator_for_search.get_page(page)

        return render(request, 'shop/index.html', {'products': paginator_sorted_products})

    paginator = Paginator(products, 12)
    paginator_products = paginator.get_page(page)

    return render(request, 'shop/index.html', {'products': paginator_products})


def details(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'shop/details.html', {'product': product})
