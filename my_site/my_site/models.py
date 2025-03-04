from django.db import models
from django.contrib.auth.models import User
from django.db.models import BigAutoField, DateTimeField
from django.forms import CharField, DecimalField



class MyUser(User):
    number = models.CharField(length = 11)
    birthday = models.DateTimeField
    sex = models.BooleanField

class Address(models.Model):
    city = CharField(max_length=128)
    street = CharField(max_length=128)
    house = CharField(max_length=4)

    user_id = models.ForeignKey(
        MyUser, on_delete=models.DO_NOTHING,
        null=True
    )

class Cards(models.Model):
    number = CharField(length=16)
    expiry_date = DateTimeField
    CVV = BigAutoField()
    user_id = models.ForeignKey(
        MyUser, on_delete=models.DO_NOTHING,
        null=True
    )

class Brand(models.Model):
    name = CharField(max_length=32)
    content = CharField(max_length = 1023)
    registration_certificate = CharField(length=15)

class BrandLogo(models.Model):
    logo = CharField(max_length=256)

    brand_id = models.ForeignKey(
        Brand, on_delete=models.DO_NOTHING,
        null=True
    )

class Product(models.Model):
    name = CharField(max_length=32)
    price = DecimalField(max_digits = 11, decimal_places = 3)
    content = CharField(max_length = 1023)
    quantity = BigAutoField()

    brand_id = models.ForeignKey(
        Brand, on_delete=models.DO_NOTHING,
        null=True
    )

class ProductImage(models.Model):
    img = CharField(max_length=256)

    product_id = models.ForeignKey(
        Product, on_delete=models.DO_NOTHING,
        null=True
    )

class Review(models.Model):
    evaluation = BigAutoField()
    content = CharField(max_length=1023)

    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        null=True
    )

    user_id = models.ForeignKey(
        MyUser, on_delete=models.CASCADE,
        null=True
    )

class ReviewPic(models.Model):
    img = CharField(max_length=513)

    review_id = models.ForeignKey(
        Review, on_delete=models.CASCADE,
        null=True
    )

class Basket(models.Model):
    user_id = models.ForeignKey(
        MyUser, on_delete=models.CASCADE,
        null=True
    )

    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        null=True
    )

class Favourite(models.Model):
    user_id = models.ForeignKey(
        MyUser, on_delete=models.CASCADE,
        null=True
    )

    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        null=True
    )