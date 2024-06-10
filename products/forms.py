from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Inventory


class ProductForm(forms.ModelForm):
    """ Form for admin to add products"""
    class Meta:
        model = Product
        # dunder method __all__ will include all fields
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        # using list comprehension to create a list of friendly names
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class InventoryForm(forms.ModelForm):
    """ Form for admin to update inventory """
    class Meta:
        model = Inventory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'