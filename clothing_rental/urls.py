from django.urls import path, include
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views


app_name = 'clothing_rental'  # เพิ่ม namespace


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('shop_detail/', views.shop_detail, name='shop_detail'),  # ✅ ใช้ `_` ไม่ใช่ `-`
    path('shop_listing/', views.shop_listing, name='shop_listing'),
    path('login/', views.user_login, name='login'),  # เพิ่ม URL สำหรับหน้า login
    path('signup/', views.user_signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),  # หน้าแรกที่จะแสดงชื่อผู้ใช้


]