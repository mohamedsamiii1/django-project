from django.urls import path
from . import views


urlpatterns =  [
path("index", views.IndexPage, name="Index"),
path("trainer", views.trainer, name="Trainer"),
path("why", views.why, name="Why"),
path("contact", views.contact, name="Contact"),
path("register", views.registrationpage, name="Registration"),
path("login", views.loginpage, name="Login"),
path("logout", views.userLogout, name="Logout"),




]