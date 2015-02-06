from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.

# All below classes deal with answers and products
class Answer (models.Model) :
	question1= models.CharField(max_length = 20)
	question2= models.CharField(max_length = 20)
	question3= models.CharField(max_length = 20)
	question4= models.CharField(max_length = 20)
	def __unicode__(self):
		return self.question1 + ', ' + self.question2 + ', ' + self.question3 + ', ' + self.question4
		
class Ingredient (models.Model):
	inType = models.CharField(max_length = 20)
	ingreName = models.CharField(max_length = 50)
	description = models.CharField(max_length = 100)
	def __unicode__(self):
		return self.ingreName + ': ' + self.description
		
class Product (models.Model):
	price = models.DecimalField(max_digits=18, decimal_places=2, verbose_name=_('price'))
	ingredient1 = models.ForeignKey(Ingredient, related_name='ingredient_cream')
	ingredient2 = models.ForeignKey(Ingredient, related_name='ingredient_penetrate')

# All below classes deal with users, their products and their purchase
class Skinuser (models.Model):
	user = models.OneToOneField(User)
	birthday = models.DateField()
	firstname = models.CharField(max_length = 100)
	lastname = models.CharField(max_length = 100)
	def __unicode__(self):
		return self.firstname + ' ' + self.lastname
	def getProducts(self):
		userprofiles = self.userproduct_set.all()
		profiles = []
		for profile in userprofiles:
			profiles.append(profile.profile)
		return profiles
	def getAddresses(self):
		useraddresses = self.useraddress_set.all()
		addresses = []
		for address in useraddresses:
			addresses.append(address.address)
		return addresses

#deals with ordering and carts
class Shippingaddress (models.Model):
	name = models.CharField(max_length = 100)
	street1 = models.CharField(max_length = 100)
	street2 = models.CharField(max_length = 100, null=True, blank=True)
	city = models.CharField(max_length = 100)
	state = models.CharField(max_length = 100)
	zipcode = models.CharField(max_length = 5)
	email = models.CharField(max_length = 100)

	def getInfo(self):
		address = ""
		address = address+self.name + "\n"+self.street1+"\n"
		if self.street2:
			address = address + self.street2+"\n"
		address = address + self.city + ", "
		address = address+self.state+" " + self.zipcode + "\n email: "+self.email
		return address

#one to many relationships
class Useraddress (models.Model):
	skinuser = models.ForeignKey(Skinuser)
	address = models.ForeignKey(Shippingaddress)