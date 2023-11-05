from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login,name='logreg'),
    path('regist/',views.regist,name='regist'),
]
