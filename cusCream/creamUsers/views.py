from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import get_list_or_404, get_object_or_404
from creamUsers.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from creamUsers.forms import RegistrationForm, LoginForm
from carton.cart import Cart
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings

############################Build Product & Select Answer#####################

def selectAnswers(request):
	# name of the input type is the post value
	# getting all values in the form
	try:
		answer1=request.POST['button1']
		answer2=request.POST['button2']
		answer3=request.POST['button3']
		answer4=request.POST['button4']
	except (KeyError, Choice.DoesNotExist):
				# Redisplay the step 1 selection form.
		return render(request, 'creamUsers/build.html', {'error_message': "We apologize that some of your choice is not captured correctly. Please build your skin profile again.",})						  
	else:
		# create the answer object and save it to the database
		a = Answer(question1 = answer1, question2 = answer2, question3 = answer3, question4 = answer4)
		a.save()
	
		# from the answer, deduce what ingredients and product the customer should use
		ingredient1 = ""
		if answer2=="morning":
			ingredient1 = "Thin"
		elif answer2=="allday":
			ingredient1="Regular"
		else:
			ingredient1="Thick"
			
		ingredient2=""
		if answer1=="dry" or answer1=="normal":
			ingredient2="Glycerin"
		else:
			ingredient2="Propylene Glycol"
			
		# create the product based on the two ingredients to display on the build2.html (result page)
		ingre1 = Ingredient.objects.get(inType="CreamBase", ingreName=ingredient1)
		ingre2 = Ingredient.objects.get(inType="PenetrateAgent", ingreName=ingredient2)
		prod = Product.objects.get(ingredient1=ingre1, ingredient2=ingre2)
		
		# return to the product result page
		return HttpResponseRedirect(reverse('creamUsers:result', args=(prod.id,a.id,)))
	
def result (request, product_id, answer_id):
	prod = get_object_or_404(Product, pk=product_id)
	answer = get_object_or_404(Answer, pk=answer_id)
	return render(request, 'creamUsers/prodResult.html', {'product' : prod, 'ingredient1':prod.ingredient1, 'ingredient2':prod.ingredient2, 'answer':answer,})
	
def resultNoAnswer (request, product_id):
	prod = get_object_or_404(Product, pk=product_id)
	return render(request, 'creamUsers/prodResult.html', {'product' : prod, 'ingredient1':prod.ingredient1, 'ingredient2':prod.ingredient2,})
	
def editProd(request, product_id):
	prod = get_object_or_404(Product, pk=product_id)
	return render (request,'creamUsers/editProd.html', {'product': prod, 'ingredient1':prod.ingredient1, 'ingredient2':prod.ingredient2, 'ingredients':Ingredient.objects.all(),} )
	
def saveEditResult(request, product_id):
	prod = get_object_or_404(Product, pk=product_id)
	try:
		ingre1 = Ingredient.objects.get(pk=request.POST['base'])
		ingre2 = Ingredient.objects.get(pk=request.POST['penetrate'])
	except (KeyError, Ingredient.DoesNotExist):
				# Redisplay the step 1 selection form.
		return render(request, 'creamUsers/editProd.html', {'product': prod, 'ingredient1':prod.ingredient1, 'ingredient2':prod.ingredient2, 'ingredients':Ingredient.objects.all(), 'error_message': "You didn't select a choice.",})
	else:
		prod = Product.objects.get(ingredient1=ingre1, ingredient2=ingre2)
		return HttpResponseRedirect(reverse('creamUsers:resultNoAnswer', args=(prod.id,)))


#############################Registration/Login Code##########################

@login_required
def UserProfile(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login/')
	skinuser = request.user.get_profile
	context = {'skinuser' : skinuser}
	return render_to_response('creamUsers/userInfo.html', context,context_instance = RequestContext(request))


def CreamUserRegistration(request):
	if request.GET:
		next = request.GET['next']
	else:
		next = None
	if request.user.is_authenticated():
		return HttpResponseRedirect('/users/')
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(username=form.cleaned_data['username'], email = form.cleaned_data['email'], password = form.cleaned_data['password'])
			user.save()
			skinuser= Skinuser(user=user, firstname = form.cleaned_data['firstname'], lastname=form.cleaned_data['lastname'], birthday=form.cleaned_data['birthday'])
			skinuser.save()
			messages.add_message(request, messages.INFO, 'Thank you for registering! Please continue to login:')
			if next and next != "None":
				return HttpResponseRedirect('/login/?next=%s' % next)
			else:
				return HttpResponseRedirect('/login/')
		else:
			return render_to_response('creamUsers/register.html', {'form':form}, context_instance = RequestContext (request))
	else:
		#user is not submitting the form, show them a blank registration form
		form = RegistrationForm()
		context = {'form':form}
		return render_to_response('creamUsers/register.html', context, context_instance = RequestContext(request))
 

def LoginRequest(request):
	if request.GET:
		next = request.GET['next']
	else:
		next = None
	if request.user.is_authenticated():
		return HttpResponseRedirect('/users/')
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			skinuser = authenticate(username=username, password = password)
			if skinuser is not None:
				login(request,skinuser)
				# if there is cart items, add all products in the userProfile
				cart = Cart(request.session)
				for product in cart.products:
					userproduct = Userproduct(skinuser = skinuser, product = product)
					userproduct.save()
				
				## deals with loading logging page
				if next:
					# redirect to the previous page
					return HttpResponseRedirect('/%s' % next)
				else:
					return HttpResponseRedirect('/users/')
			else:
				return render_to_response('creamUsers/login.html', {'form':form, 'next': next,'error_message': "Username and Password are incorrect",}, context_instance = RequestContext (request))
		else:
			return render_to_response('creamUsers/login.html', {'form':form, 'next': next,}, context_instance = RequestContext (request))
	else:
		#user is not submitting the form, show the login form
		form = LoginForm()
		return render_to_response('creamUsers/login.html', {'form':form, 'next': next,}, context_instance = RequestContext (request))

def LogoutRequest(request):
	logout(request)
	return HttpResponseRedirect('/')

##################Below Code Deal With Carts##################################
def Cartdetail(request):
	return render(request, 'creamUsers/cart.html')
	
def AddProduct (request, product_id):
	prod = get_object_or_404(Product, pk=product_id)
	cart = Cart(request.session)
	cart.add(prod, prod.price)
	if request.user.is_authenticated():
		skinuser = request.user.skinuser
		if prod not in skinuser.getProducts():
			userproduct = Userproduct(skinuser = skinuser, product = prod)
			userproduct.save()
	return HttpResponseRedirect(reverse('creamUsers:cartdetail'))

def Plusone (request, product_id):
	prod = get_object_or_404(Product, pk=product_id)
	cart = Cart(request.session)
	cart.add(prod, prod.price)
	return HttpResponseRedirect(reverse('creamUsers:cartdetail'))

def Minusone (request, product_id):
	prod = get_object_or_404(Product, pk=product_id)
	cart = Cart(request.session)
	cart.remove_single(prod)
	return HttpResponseRedirect(reverse('creamUsers:cartdetail'))

def Removeproduct (request, product_id):
	prod = get_object_or_404(Product, pk=product_id)
	cart = Cart(request.session)
	cart.remove(prod)
	if request.user.is_authenticated():
		skinuser = request.user.skinuser
		if prod in skinuser.getProducts():
			up = Userproduct.objects.get(skinuser = skinuser, product = prod)
			up.delete()
	return HttpResponseRedirect(reverse('creamUsers:cartdetail'))
	
#########################Below Code is Created for Paypal#####################
def checkOutWithPaypal(request):

	cart = Cart(request.session)
	money = cart.total
	# What you want the button to do.
	paypal_dict = {
		"business": settings.PAYPAL_RECEIVER_EMAIL,
		"amount": money,
		"item_name": "name of the item",
		"invoice": "unique-invoice-id",
		"notify_url": reverse('paypal:paypal-ipn'),
		"return_url": "/",
		"cancel_return": "/",

	}

	# Create the instance.
	form = PayPalPaymentsForm(initial=paypal_dict)
	context = {"form": form}
	return render_to_response("creamUsers/payment.html", context)