from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.Home,name="Home" ),
    path('accounts/login/',views.Login,name="Login" ),
    path('employee_view/',views.Employee_View,name="Employee_View" ),
     path('attendence/',views.Attendence,name="Attendence" ),
     path('add_employee/',views.AddEmployee,name="AddEmployee" ),
    path('logout/',views.Logout,name="Logout" ),
    path('register/',views.Register,name="Register" ),
    path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
]