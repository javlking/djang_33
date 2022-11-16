from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=220)

    def __str__(self): # Нормальное отображение категорий
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=220)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_description = models.TextField()
    product_price = models.FloatField()
    product_quantity = models.IntegerField()

    def __str__(self):
        return self.product_name


class Sale(models.Model):
    sale_name = models.CharField(max_length=150)
    sale_products = models.ManyToManyField(Product)
    sale_start_date = models.DateTimeField()
    sale_end_date = models.DateTimeField()
    sale_percent = models.FloatField()

    def __str__(self):
        return self.sale_name

class Cart(models.Model):
    user_id = models.IntegerField()
    user_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_quantity = models.IntegerField()
    total_for_current_product = models.FloatField()


class Feedback(models.Model):
    user_mail = models.EmailField(null=True, blank=True)
    feedback_message = models.TextField()
    feedback_date = models.DateTimeField(auto_now_add=True)


