from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .models import Food, Ingredient, PotentialRisk
from .ai_utils import generate_food_data

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
def check_food_safety(request):
    food_name = request.GET.get('food_name')
    pregnancy_week = int(request.GET.get('pregnancy_week'))

    try:
        # DB에서 음식 정보 조회
        food = Food.objects.get(name=food_name)
    except Food.DoesNotExist:
        # 없으면 AI 생성 후 저장
        food_data = generate_food_data(food_name)
        food = Food.objects.create(name=food_name, kcal=int(food_data['kcal']))

        for ingredient_data in food_data['ingredients']:
            ingredient, created = Ingredient.objects.get_or_create(name=ingredient_data['name'])
            food.ingredients.add(ingredient)
            # PotentialRisk 정보 추가
            for risk_data in ingredient_data.get('potential_risks', []):
                PotentialRisk.objects.create(
                    ingredient=ingredient, pregnancy_week_start=risk_data['week_start'],
                    pregnancy_week_end=risk_data['week_end'], risk_level=risk_data['risk_level'])
    risks = []

    # 음식 성분별 위험성 평가
    for ingredient in food.ingredients.all():
        potential_risks = PotentialRisk.objects.filter(
            ingredient=ingredient, pregnancy_week_start__lte=pregnancy_week, pregnancy_week_end__gte=pregnancy_week)
        for risk in potential_risks:
            risks.append({
                'ingredient': ingredient.name,
                'risk_level': risk.risk_level
            })

    context = {
        'food': food,
        'risks': risks,
        'pregnancy_week': pregnancy_week
    }
    return render(request, 'mommymomeatsapp/food_safety.html', context)
