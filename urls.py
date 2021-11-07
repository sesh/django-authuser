from django.conf.urls import url

from .views import logout, signup


urlpatterns = [
    url(r"^logout/", logout, name="logout"),
    url(r"^signup/", signup, name="signup"),
]
