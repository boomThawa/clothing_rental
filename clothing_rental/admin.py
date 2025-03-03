from django.contrib import admin
from .models import UserProfile, Product  # เพิ่มโมเดลที่ต้องการจัดการใน Admin

# ลงทะเบียนโมเดล UserProfile
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address')  # กำหนดฟิลด์ที่จะให้แสดงในหน้า admin
    search_fields = ('user__username',)  # สามารถค้นหาผ่านชื่อผู้ใช้ได้

# ลงทะเบียนโมเดล Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')  # กำหนดฟิลด์ที่จะแสดงในหน้า admin
    search_fields = ('name',)  # สามารถค้นหาผ่านชื่อสินค้าได้

# ลงทะเบียนโมเดลใน Admin
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Product, ProductAdmin)
