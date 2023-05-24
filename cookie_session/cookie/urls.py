from django.urls import path
from . import views



urlpatterns = [
    path('cset/', views.cookieset),
    path('cget/', views.cookieget),
    path('cdlt/', views.cookiedlt),
]