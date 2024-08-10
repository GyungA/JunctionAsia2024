from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('check-food/', views.check_food, name='check_food'),
    path('check-food-safety/', views.check_food_safety, name='check_food_safety'),
]
