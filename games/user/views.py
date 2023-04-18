from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import CreateView
from .forms import RegisterForm


class RegisterView(CreateView):
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')
    form_class = RegisterForm
