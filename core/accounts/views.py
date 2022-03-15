from django.shortcuts import render, redirect
from django.views import View
from django.contribut.auth import login, authenticate, logout


class LoginView(View):
    template_name = "accounts/login.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


class SignUpView(View):
    template_name = "accounts/sign-up.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('accounts:login')
