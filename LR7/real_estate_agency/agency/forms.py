from django import forms
from django.contrib.auth.models import User
from .models import Deal, Buyer, Realtor, UserProfile
import re

class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['buyer', 'realtor', 'property_address', 'price', 'deal_date']
        widgets = {
            'deal_date': forms.DateInput(attrs={'type': 'date'}),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
        }

    def clean_property_address(self):
        address = self.cleaned_data['property_address']
        if len(address) < 5:
            raise forms.ValidationError("Адрес недвижимости должен содержать не менее 5 символов.")
        return address

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("Цена должна быть больше 0.")
        return price

class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['first_name', 'last_name', 'patronymic', 'phone', 'email']

    def clean_first_name(self):
        name = self.cleaned_data['first_name']
        if not re.match(r'^[А-Я][а-я]*$', name):
            raise forms.ValidationError("Имя должно начинаться с прописной буквы, содержать только кириллицу.")
        return name

    def clean_last_name(self):
        name = self.cleaned_data['last_name']
        if not re.match(r'^[А-Я][а-я]*$', name):
            raise forms.ValidationError("Фамилия должна начинаться с прописной буквы, содержать только кириллицу.")
        return name

    def clean_patronymic(self):
        name = self.cleaned_data['patronymic']
        if not re.match(r'^[А-Я][а-я]*$', name):
            raise forms.ValidationError("Отчество должно начинаться с прописной буквы, содержать только кириллицу.")
        return name

    def clean_email(self):
        email = self.cleaned_data['email']
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            raise forms.ValidationError("Некорректный формат email.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not re.match(r'^\+?\d{10,15}$', phone):
            raise forms.ValidationError("Телефон должен содержать от 10 до 15 цифр, возможно с '+'.")
        return phone

class RealtorForm(forms.ModelForm):
    class Meta:
        model = Realtor
        fields = ['first_name', 'last_name', 'patronymic', 'phone', 'email', 'experience_years']
        widgets = {
            'experience_years': forms.NumberInput(attrs={'min': 0}),
        }

    def clean_first_name(self):
        name = self.cleaned_data['first_name']
        if not re.match(r'^[А-Я][а-я]*$', name):
            raise forms.ValidationError("Имя должно начинаться с прописной буквы, содержать только кириллицу.")
        return name

    def clean_last_name(self):
        name = self.cleaned_data['last_name']
        if not re.match(r'^[А-Я][а-я]*$', name):
            raise forms.ValidationError("Фамилия должна начинаться с прописной буквы, содержать только кириллицу.")
        return name

    def clean_patronymic(self):
        name = self.cleaned_data['patronymic']
        if not re.match(r'^[А-Я][а-я]*$', name):
            raise forms.ValidationError("Отчество должно начинаться с прописной буквы, содержать только кириллицу.")
        return name

    def clean_email(self):
        email = self.cleaned_data['email']
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            raise forms.ValidationError("Некорректный формат email.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not re.match(r'^\+?\d{10,15}$', phone):
            raise forms.ValidationError("Телефон должен содержать от 10 до 15 цифр, возможно с '+'.")
        return phone

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Подтверждение пароля")

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Имя пользователя уже занято.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            raise forms.ValidationError("Некорректный формат email.")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email уже используется.")
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if not re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password):
            raise forms.ValidationError(
                "Пароль должен быть не менее 8 символов, содержать прописные и строчные буквы, цифры и специальные символы."
            )
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают.")
        return cleaned_data

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'patronymic', 'role']

    def clean_first_name(self):
        name = self.cleaned_data['first_name']
        if not re.match(r'^[А-Я][а-я]*$', name):
            raise forms.ValidationError("Имя должно начинаться с прописной буквы, содержать только кириллицу.")
        return name

    def clean_last_name(self):
        name = self.cleaned_data['last_name']
        if not re.match(r'^[А-Я][а-я]*$', name):
            raise forms.ValidationError("Фамилия должна начинаться с прописной буквы, содержать только кириллицу.")
        return name

    def clean_patronymic(self):
        name = self.cleaned_data['patronymic']
        if not re.match(r'^[А-Я][а-я]*$', name):
            raise forms.ValidationError("Отчество должно начинаться с прописной буквы, содержать только кириллицу.")
        return name