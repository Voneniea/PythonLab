from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    USER_ROLES = (
        ('admin', 'Администратор'),
        ('user', 'Обычный пользователь'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=50, verbose_name="Отчество")
    role = models.CharField(max_length=10, choices=USER_ROLES, default='user', verbose_name="Роль")

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic} ({self.user.username})"

    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"

class Buyer(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=50, verbose_name="Отчество")
    phone = models.CharField(max_length=15, verbose_name="Телефон")
    email = models.EmailField(unique=True, verbose_name="Email")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Создал")

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"

class Realtor(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=50, verbose_name="Отчество")
    phone = models.CharField(max_length=15, verbose_name="Телефон")
    email = models.EmailField(unique=True, verbose_name="Email")
    experience_years = models.PositiveIntegerField(verbose_name="Стаж (годы)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Создал")

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    class Meta:
        verbose_name = "Риелтор"
        verbose_name_plural = "Риелторы"

class Deal(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, verbose_name="Покупатель")
    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE, verbose_name="Риелтор")
    property_address = models.CharField(max_length=200, verbose_name="Адрес недвижимости")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    deal_date = models.DateField(verbose_name="Дата сделки")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Создал")

    def __str__(self):
        return f"Сделка {self.id} - {self.property_address}"

    class Meta:
        verbose_name = "Сделка"
        verbose_name_plural = "Сделки"