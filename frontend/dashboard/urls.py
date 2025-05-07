from django.urls import path
from . import views

urlpatterns = [
    path('', views.match_form, name='match_form'),
    path('predict-score/', views.score_form, name='score_form'),
]
