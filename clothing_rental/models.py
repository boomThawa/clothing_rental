from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


# 🧑‍💼 1. ข้อมูลโปรไฟล์ลูกค้า
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, verbose_name=_("Phone Number"))
    address = models.TextField(verbose_name=_("Address"))
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True, verbose_name=_("Profile Picture"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profiles")

# 🏷 2. หมวดหมู่ชุด
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Category Name"))
    description = models.TextField(blank=True, verbose_name=_("Description"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

# 👗 3. รายละเอียดชุดให้เช่า
class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Product Name"))
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name=_("Category"))
    description = models.TextField(verbose_name=_("Description"))
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price per Day"))
    stock = models.PositiveIntegerField(default=1, verbose_name=_("Stock Available"))
    image = models.ImageField(upload_to='product_images/', blank=True, null=True, verbose_name=_("Product Image"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))

    def __str__(self):
        return f"{self.name} - {self.category.name}"

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

# 📅 4. รายการเช่าชุด
class Rental(models.Model):  # เปลี่ยนชื่อคลาสจาก rental เป็น Rental
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))
    start_date = models.DateField(verbose_name=_("Start Date"))
    end_date = models.DateField(verbose_name=_("End Date"))
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Total Price"))
    status_choices = [
        ('pending', _("Pending")),
        ('confirmed', _("Confirmed")),
        ('returned', _("Returned")),
        ('canceled', _("Canceled"))
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='pending', verbose_name=_("Status"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))

    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.status})"

    class Meta:
        verbose_name = _("clothing_rental")
        verbose_name_plural = _("clothing_rentals")


# 💳 5. รายละเอียดการชำระเงิน
class Payment(models.Model):
    rental = models.OneToOneField(Rental, on_delete=models.CASCADE, verbose_name=_("Rental"))
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Payment Date"))
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Amount"))
    payment_method = models.CharField(max_length=50, verbose_name=_("Payment Method"))
    status_choices = [
        ('pending', _("Pending")),
        ('completed', _("Completed")),
        ('failed', _("Failed"))
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='pending', verbose_name=_("Payment Status"))

    def __str__(self):
        return f"Payment {self.id} - {self.rental.user.username}"

    class Meta:
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")


# ⭐ 6. รีวิวจากลูกค้า
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))
    rating = models.PositiveIntegerField(default=5, verbose_name=_("Rating"))
    comment = models.TextField(blank=True, null=True, verbose_name=_("Comment"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))

    def __str__(self):
        return f"Review by {self.user.username} - {self.product.name} ({self.rating}⭐)"

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")

    def save(self, *args, **kwargs):
        if self.end_date < self.start_date:
            raise ValidationError(_("End date cannot be earlier than start date"))
        super().save(*args, **kwargs)

