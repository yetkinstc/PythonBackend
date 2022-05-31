
from django.urls import path
from . import views


urlpatterns = [
    path("feed",views.feed, name="feed"),
    path("login",views.login, name="login"),
    path("signUp",views.signUp, name="signUp"),
    path("",views.login, name="login"),
    path("signUp2",views.signUp2, name="signUp2"),
    path("myP",views.myP, name="myP"),
    path("logout",views.logout, name="login"),
]