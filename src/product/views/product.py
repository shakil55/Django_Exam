from django.views import generic
from django.shortcuts import render, redirect
from product.models import Variant, Product
from product.forms import ProductForm

class CreateProductView(generic.TemplateView):
    template_name = 'backend/products/create_product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['variants'] = [(variant.id, variant.title) for variant in Variant.objects.filter(active=True)]
        return context

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            selected_variant = request.POST.get('variants')
            if selected_variant:
                product.variants.add(selected_variant)
            return redirect('success_url')  # Replace 'success_url' with your actual success URL
    else:
        form = ProductForm()
    return render(request, 'backend/products/create_product.html', {'form': form})


from django.views.generic import TemplateView
from product.models import Product

class ProductListView(TemplateView):
    template_name = 'backend/products/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        if products.exists():
            context['products'] = products
        else:
            context['message'] = 'There are no products in the database.'
        return context