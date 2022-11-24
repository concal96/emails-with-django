from django.urls import path
from email_app import views

urlpatterns = [
    path('',views.thanks,name='thanks')
]