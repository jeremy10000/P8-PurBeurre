from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


""" 
	for templates
	login:<name>

"""
app_name = 'login'

urlpatterns = [
    path('', LoginView.as_view(), name="connect"),
    path('logout/', LogoutView.as_view(), name="disconnect"),
    #path('join/', views.SignUp.as_view(), name="join"),
    #path('mypage/', views.mypage, name="mypage"),
]
