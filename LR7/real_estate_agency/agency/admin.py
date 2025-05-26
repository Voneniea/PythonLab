from django.contrib import admin
from .models import Buyer, Realtor, Deal, UserProfile

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'patronymic', 'email', 'phone', 'created_at', 'created_by')
    list_filter = ('created_at',)
    search_fields = ('last_name', 'first_name', 'email')
    ordering = ('last_name',)

@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'patronymic', 'email', 'phone', 'experience_years', 'created_by')
    list_filter = ('experience_years', 'created_at')
    search_fields = ('last_name', 'first_name', 'email')
    ordering = ('last_name',)

@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('id', 'buyer', 'realtor', 'property_address', 'price', 'deal_date', 'created_by')
    list_filter = ('deal_date', 'realtor')
    search_fields = ('property_address', 'buyer__last_name', 'realtor__last_name')
    ordering = ('-deal_date',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'last_name', 'first_name', 'patronymic', 'role')
    list_filter = ('role',)
    search_fields = ('user__username', 'last_name', 'first_name')