from django.contrib import admin

# Register your models here.
from cart import models

admin.site.register(models.Cart)
admin.site.register(models.Item)
