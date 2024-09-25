from todo import views
from django.urls import path

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path("signup/", views.signup, name="signup"),
    path('edit_todo/<int:pk>/', views.edit_todo, name='edit_todo'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete_todo'),
    path('', views.home, name='home'),
]
