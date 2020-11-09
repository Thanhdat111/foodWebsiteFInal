from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import UserProfileInfo, Meats, Groceries, Meals, Fishandmeatandeggs
from .form import RegisterForm


# Create your views here.


def store(request):
    username = request.user.username
    user_id = request.user.id
    try:
        userProfile = UserProfileInfo.objects.get(user_id=user_id)
    except Exception as e:
        userProfile = None

    # meats = Meats.objects.raw('SELECT * FROM fooddata.pickles')
    try:
        target = userProfile.target
    except Exception as e:
        target = None

    # print(target)
    if target == 1:
        meats = Meats.objects.raw(sqlQueryStringForPatient('meats'))
        groceries = Groceries.objects.raw(sqlQueryStringForPatient('groceries'))
        meals = Meats.objects.raw(sqlQueryStringForPatient('meals'))
        fishandmeatandeggs = Fishandmeatandeggs.objects.raw(sqlQueryStringForPatient('Fishandmeatandeggs'))
        bad_meats = Meats.objects.raw(sqlBadFoodForPatient('meats'))
        bad_grooceries = Groceries.objects.raw(sqlBadFoodForPatient('groceries'))
        bad_meals = Meals.objects.raw(sqlBadFoodForPatient('meals'))
        bad_fishandmeatandeggs = Fishandmeatandeggs.objects.raw(sqlBadFoodForPatient('Fishandmeatandeggs'))
    if target == 0:
        meats = Meats.objects.all()
        groceries = Groceries.objects.all()
        meals = Meals.objects.all()
        fishandmeatandeggs = Fishandmeatandeggs.objects.all()
        bad_meats = None
        bad_grooceries = None
        bad_meals = None
        bad_fishandmeatandeggs = None
    if target is None:
        meats = None
        groceries = None
        meals = None
        fishandmeatandeggs = None
        bad_meats = None
        bad_grooceries = None
        bad_meals = None
        bad_fishandmeatandeggs = None

    # meats = getDataForPatient(Meats)
    context = {'username': username,
               'userId': user_id,
               'userProfiler': userProfile,
               'target': target,
               'meats': meats,
               'groceries': groceries,
               'meals': meals,
               'fishandmeatandeggs': fishandmeatandeggs,
               'bad_meats': bad_meats,
               'bad_grooceries': bad_grooceries,
               'bad_meals': bad_meals,
               'bad_fishandmeatandeggs': bad_fishandmeatandeggs
               }

    # print(request.user.id)
    # print(userProfile.cp)
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


def sqlQueryStringForPatient(catalog):
    return 'SELECT * FROM fooddata.' + catalog + ' where ' \
                                                 'vitamin_b1 is not null ' \
                                                 'or vitamin_b2 is not null ' \
                                                 'or vitamin_b12 is not null ' \
                                                 'or vitamin_b6 is not null ' \
                                                 'or vitamin_b9 is not null'


def sqlQueryStringForNormal(catalog):
    return 'SELECT * FROM fooddata.' + catalog


def sqlBadFoodForPatient(catalog):
    return 'SELECT * FROM fooddata.' + catalog + ' where ' \
                                                 'fat > 25 ' \
                                                 'or energy > 20 ' \
                                                 'or cholesterol is not null '
