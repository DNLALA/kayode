from venv import create
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from . import forms
# Create your views here.


class signup(CreateView):
    form_class = forms.UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
