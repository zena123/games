from django.urls import path
from .views import RegisterView, LoginView

app_name= 'user'

urlpatterns = [
    path("registration/", RegisterView.as_view(), name="registration"),
    path("login-view/", LoginView.as_view(), name="login"),
    ]