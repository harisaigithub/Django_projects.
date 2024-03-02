from django.urls import path
from StudentApp import views

urlpatterns = [
    path('',views.stdnt, name="std"),
    path('stp/<int:z>/',views.stdup, name="stdnup"),
    path('stdt/<int:a>/',views.stdtl, name="stdd"),
]