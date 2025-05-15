from django.shortcuts import render
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/index.html')

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/login.html')

class ServiceView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/servico.html')