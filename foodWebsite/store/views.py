from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import UserProfileInfo, Meats
from .form import RegisterForm


# Create your views here.


def store(request):
    username = request.user.username
    user_id = request.user.id
    userProfile = UserProfileInfo.objects.get(user_id=user_id)
    meats = Meats.objects.raw('SELECT * FROM fooddata.pickles')
    context = {'username': username,
               'userId': id,
               'userProfiler': userProfile,
               'meats': meats}

    print(request.user.id)
    print(userProfile.cp)
    return render(request, 'store/index.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


def contact(request):
    context = {}
    return render(request, 'store/contact.html', context)


def blog(request):
    context = {}
    return render(request, 'store/blog.html', context)


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('store')
    else:
        form = RegisterForm()
    return render(request, 'store/registration.html', {'form': form})
