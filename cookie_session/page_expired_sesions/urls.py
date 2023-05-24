from django.urls import path
from . import views

urlpatterns = [
    path('sset/', views.sessionset),
    path('sget/', views.sessionget),
    path('sdlt/', views.sessiondlt),
]