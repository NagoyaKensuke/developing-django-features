from django.views.generic import ListView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'

    def get_queryset(self):
        products = Product.objects.all()
        for product in products:
            product.save()  # 価格を動的に調整
        return products
