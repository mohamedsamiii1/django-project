from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_users,adminOnly


@login_required(login_url='Login')

def contact(request):
 	return render(request,"main/contact.html")

def IndexPage(request):
	return render(request,"main/index.html")

@login_required(login_url='Login')
def why(request):
	return render(request,"main/why.html")


@login_required(login_url='Login')
def trainer(request):
	return render(request,"main/trainer.html")


@unauthenticated_user
def registrationpage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			group = Group.objects.get(name='customer')
			user.groups.add(group)
			
			username = form.cleaned_data.get("username")
			messages.success(request,"account was created "+ username)
			return redirect("Login")
	context = {'form':form}
	return render(request,"main/registrationpage.html", context)

	
	

@unauthenticated_user
def loginpage(request):	
	
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(request,username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect("Index")
		else:
			messages.info(request,"Username OR Password is Incorrect")

	return render(request,"main/loginpage.html")
	


def userLogout(request):
	logout(request)
	return redirect("Login")
	




