import hashlib
from random import random

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

from django import forms
from django.forms import ModelForm

from adminapp.validator import file_size
from authapp.models import User, UserProfile
from authapp.validator import validate_name
from mainapp.models import ProductCategories, Product


class UserAdminRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'last_name', 'first_name', 'email', 'image', 'age')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Введите пароль повторно'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите email'
        self.fields['image'].widget.attrs['placeholder'] = 'Добавить фото'
        self.fields['age'].widget.attrs['placeholder'] = 'Возраст'



        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'costom-file-input'




class UserAdminProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(), validators=[validate_name])
    image = forms.ImageField(widget=forms.FileInput(), required=False)
    age = forms.IntegerField(widget=forms.NumberInput(), required=False)
    class Meta:
        model = User
        fields = ('username', 'image', 'age', 'last_name', 'first_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'costom-file-input'





class ProductCatAdminCreateForm(ModelForm):
    is_active = forms.BooleanField(required=False, initial={'is_active': True})

    class Meta:
        model = ProductCategories
        fields = ('name', 'description', 'is_active')

    def __init__(self, *args, **kwargs):
        super(ProductCatAdminCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Имя категории'
        self.fields['description'].widget.attrs['plaseholder'] = 'Описание категории'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

class ProdAdminCreateForm(ModelForm):

    image = forms.ImageField(widget=forms.FileInput(), required=False, validators=[file_size])
    is_active = forms.BooleanField(required=False, initial={'is_active': True})

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'quantity', 'category',  'is_active')

    def __init__(self, *args, **kwargs):
        super(ProdAdminCreateForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs['placeholder'] = 'Наименование категории'
        self.fields['description'].widget.attrs['placeholder'] = 'Описание товара'
        self.fields['name'].widget.attrs['placeholder'] = 'Наименование товара'
        self.fields['price'].widget.attrs['placeholder'] = 'Цена'
        self.fields['quantity'].widget.attrs['placeholder'] = 'Количество на складе'
        self.fields['image'].widget.attrs['placeholder'] = 'Добавить фотографию'

        for field_name, field in self.fields.items():
            if field_name == 'category':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'
