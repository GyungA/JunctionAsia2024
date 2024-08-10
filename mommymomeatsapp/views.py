from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from mommymomeatsapp.forms import FoodForm


def home(request):
    return render(request, 'home.html')

# 회원 관리
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid Credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

# 음식 안전성 검사
def check_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            food = form.save()
            # TODO: 안전성 분석
            feedback = "This food is safe for consumption."
            return render(request, 'mommymomeatsapp/food_safety_check.html',
                          {'food': food, 'feedback': feedback})
    else:
        form = FoodForm()

    return render(request, 'mommymomeatsapp/food_safety_check.html', {'form': form})
