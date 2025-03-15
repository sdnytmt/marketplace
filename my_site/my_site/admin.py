from django.contrib.admin import register
from django.contrib import admin

from . import models

admin.site.register(models.MyUser)
admin.site.register(models.Address)
admin.site.register(models.Cards)
admin.site.register(models.Brand)
admin.site.register(models.BrandLogo)
admin.site.register(models.Product)
admin.site.register(models.ProductImage)
admin.site.register(models.Review)
admin.site.register(models.ReviewPic)
admin.site.register(models.Basket)
admin.site.register(models.Favourite)
