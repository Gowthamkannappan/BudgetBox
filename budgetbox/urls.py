from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),                                                        # admin Page
    path('transactions/',include('apps.transactions.urls')),                                # Path for Transcations Dashboard, Add, Delete , update
    path('users/',include('apps.users.urls')),                                              # Path for Users Login ,Signin ,Signup
]