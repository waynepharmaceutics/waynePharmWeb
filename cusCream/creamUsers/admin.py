from django.contrib import admin
from creamUsers.models import Answer, Ingredient, Product, Skinuser, Shippingaddress, Useraddress


# Register your models here.
class AnswerAdmin(admin.ModelAdmin):
	list_display = ('question1', 'question2', 'question3', 'question4')
admin.site.register(Answer, AnswerAdmin)

class IngreAdmin(admin.ModelAdmin):
	list_display = ('inType', 'ingreName', 'description')
admin.site.register(Ingredient, IngreAdmin)

class ProdAdmin(admin.ModelAdmin):
	list_display = ('ingredient1', 'ingredient2', 'price')
admin.site.register(Product,ProdAdmin)

class SkinUserAdmin(admin.ModelAdmin):
	list_display = ('user', 'birthday')
admin.site.register(Skinuser, SkinUserAdmin)

class AddressAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'street1')
admin.site.register(Shippingaddress, AddressAdmin)

admin.site.register(Useraddress)