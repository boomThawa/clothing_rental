from django.contrib import admin
from .models import UserProfile, Category, Product, Rental, Payment, Review



# 🧑‍💼 ตั้งค่าหน้า Admin สำหรับ UserProfile
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address', 'created_at')
    search_fields = ('user__username', 'phone_number')
    list_filter = ('created_at',)


# 🏷 ตั้งค่าหน้า Admin สำหรับ Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

# 👗 ตั้งค่าหน้า Admin สำหรับ Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price_per_day', 'stock', 'created_at')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')

# 📅 ตั้งค่าหน้า Admin สำหรับ Rental
@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'start_date', 'end_date', 'total_price', 'status')
    list_filter = ('status', 'start_date', 'end_date')
    search_fields = ('user__username', 'product__name')

# 💳 ตั้งค่าหน้า Admin สำหรับ Payment
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('rental', 'payment_date', 'amount', 'payment_method', 'status')
    list_filter = ('status', 'payment_method')
    search_fields = ('rental__user__username',)

# ⭐ ตั้งค่าหน้า Admin สำหรับ Review
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('user__username', 'product__name')
