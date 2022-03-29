from django.urls import path

from .views import logout, signup


urlpatterns = [
    path("logout/", logout, name="logout"),
    path("signup/", signup, name="signup"),
]
