from django.urls import path
from VVITApp import views

urlpatterns = [
    path('',views.home, name="hm"),
    path('abt/',views.about, name="ab"),
    path('reg/',views.register, name="rg"),
]