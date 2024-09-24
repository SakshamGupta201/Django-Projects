from todo import views
from django.urls import path

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path("signup/", views.signup, name="signup"),
    path('', views.home, name='home'),
]
