from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.UserSignUp.as_view(),name='user_signup'),
    path('signin/',views.UserSignIn.as_view(),name='user_signup'),
    path('profile/',views.UserProfile.as_view(),name='Profile'),
    path('updateProfile/',views.UserProfile.as_view(),name='Profile')
    
]
