from django import forms
from products.models import CategoryProducts, Products
from users.forms import UserRegisterForms, UserProfileForm
from users.models import User


class UserAdminRegisterForm(UserRegisterForms):
    image = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'image')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForms, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'image':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-control py-4'


class UserAdminProfileForm(UserProfileForm):

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = False
        self.fields['email'].widget.attrs['readonly'] = False
        for field_name, field in self.fields.items():
            if field_name == 'image':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-control py-4'


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = CategoryProducts
        fields = ('category_name', 'category_description')

    def __init__(self, *args, **kwargs):
        super(CategoryCreateForm, self).__init__(*args, **kwargs)
        self.fields['category_name'].widget.attrs['placeholder'] = 'Введите название категории'
        self.fields['category_description'].widget.attrs['placeholder'] = 'Введите описание категории'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class ProductsCreateForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('products_name', 'products_descriptions', 'products_price', 'image', 'quantity', 'category')

    def __init__(self, *args, **kwargs):
        super(ProductsCreateForm, self).__init__(*args, **kwargs)
        self.fields['products_name'].widget.attrs['placeholder'] = 'Введите название продукта'
        self.fields['products_descriptions'].widget.attrs['placeholder'] = 'Введите описание продукта'
        for field_name, field in self.fields.items():
            if field_name == 'image' or field_name == 'category' or field_name == 'quantity' or field_name == 'products_price':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-control py-4'
