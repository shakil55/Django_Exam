
from django import forms 
from product.models import Product, Variant  

class ProductForm(forms.ModelForm):
    variants = forms.ModelChoiceField(queryset=Variant.objects.filter(active=True), required=False)  

    class Meta:
        model = Product
        fields = ('title', 'sku', 'description', 'variants')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Populate choices for variants field dynamically
        self.fields['variants'].queryset = Variant.objects.filter(active=True)

class VariantForm(forms.ModelForm):
    class Meta:
        model = Variant
        fields = ('title', 'description', 'active') 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)