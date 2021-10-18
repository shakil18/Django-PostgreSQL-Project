from django.shortcuts import redirect, render
from .models import Feature, BloodBankUserDb
from django.contrib.auth.models import User, auth
from django.contrib import messages


def index(request):
    # features1 = Feature()
    # features1.name = 'I\'m 1'
    # features1.details = 'our service is very quick'

    # features2 = Feature()
    # features2.name = 'I\'m 2'
    # features2.details = 'our service is very quick'

    # features3 = Feature()
    # features3.name = 'I\'m 3'
    # features3.details = 'our service is very quick'

    # features = [features1, features2, features3]

    # context = {
    #     'new_key': 'asf*&%^858qqjlkj',
    #     'new_age': 17,
    #     'features':features
    # }

    features_obj = Feature.objects.all()
    return render(request, 'index.html', {'features_obj':features_obj})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not the same')
            return redirect('register')

    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect ('login')

    else: 
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def database(request):
    database_obj = BloodBankUserDb.objects.all()

    return render(request, 'database.html', {'databaseobj':database_obj})


def post(request, value):
    return render(request, 'post.html', {'pk':value})


def archive(request):
    years = [2015,2016,2017,2018,2019,2020,2021]

    return render(request,'archive.html',{'years':years})