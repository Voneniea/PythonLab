from django.urls import path
from . import views

app_name = 'agency'

urlpatterns = [
    path('', views.deal_list, name='deal_list'),
    path('deal/add/', views.deal_create, name='deal_create'),
    path('deal/<int:pk>/', views.deal_detail, name='deal_detail'),
    path('deal/<int:pk>/edit/', views.deal_edit, name='deal_edit'),
    path('deal/<int:pk>/delete/', views.deal_delete, name='deal_delete'),
    path('buyer/', views.buyer_list, name='buyer_list'),
    path('buyer/add/', views.buyer_create, name='buyer_create'),
    path('buyer/<int:pk>/', views.buyer_detail, name='buyer_detail'),
    path('buyer/<int:pk>/edit/', views.buyer_edit, name='buyer_edit'),
    path('buyer/<int:pk>/delete/', views.buyer_delete, name='buyer_delete'),
    path('realtor/', views.realtor_list, name='realtor_list'),
    path('realtor/add/', views.realtor_create, name='realtor_create'),
    path('realtor/<int:pk>/', views.realtor_detail, name='realtor_detail'),
    path('realtor/<int:pk>/edit/', views.realtor_edit, name='realtor_edit'),
    path('realtor/<int:pk>/delete/', views.realtor_delete, name='realtor_delete'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('deals/export/excel/', views.export_deals_excel, name='export_deals_excel'),
    path('deals/export/word/', views.export_deals_word, name='export_deals_word'),
    path('deals/export/pdf/', views.export_deals_pdf, name='export_deals_pdf'),
]