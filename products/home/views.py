from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect 
from .forms import ContactForm, LoginForm, RegisterForm
from product.models import Product
User = get_user_model()
# Create your views here.

def home_page(request):
   # print(request.session.get("first_name", "Unknown"))
    context={
    }
    if request.user.is_authenticated:
        queryset = Product.objects.filter(featured=True)
        context = {
            'object_list': queryset
        }
    return render(request, "home_page.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    }
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            print(request.user.is_authenticated)
            #context['form'] = LoginForm()
            return redirect("/home")
        else:
            print("Error")
    return render(request, "auth/login.html", context)

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
        return redirect("/login")

    return render(request, "auth/register.html", context)

def view(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    #if request.method=="POST":
        #print(request.POST)
        #print(request.POST.get('fullname'))
        #print(request.POST.get('email'))
    return render(request, "contact/view.html", context)

def _logout(request):
    logout(request)
    return render(request, "home_page.html", {'premium_content': 'Login again'})