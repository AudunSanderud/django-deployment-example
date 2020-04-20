from django.urls import path
from form import views

urlpatterns = [
    path('', views.form_name, name='form_name')
]
