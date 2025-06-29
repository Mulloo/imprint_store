from django import forms
from .models import Product, Category, ProductReview, Tag
from .widgets import CustomClearableFileInput

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        
        # Make tags field use checkboxes for multiple selection
        self.fields['tags'].widget = forms.CheckboxSelectMultiple()
        self.fields['tags'].queryset = Tag.objects.filter(is_active=True)
        
        for field_name, field in self.fields.items():
            if field_name != 'tags':  # Don't apply border-black to checkboxes
                field.widget.attrs['class'] = 'border-black rounded-0'



class ReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ("title", "content", "rating")
        widgets = {
            "title":   forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows":4}),
            "rating":  forms.Select(attrs={"class": "form-control"}),
        }
