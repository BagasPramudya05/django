from django.urls import path

from app import views

urlpatterns=[
	path('',views.home,name="home"),
	path('wordcalci.html',views.wordcalci,name="wordcalci"),
]