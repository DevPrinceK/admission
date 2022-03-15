from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


class LoginView(View):
    template_name = "accounts/login.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('index_number')
        password = request.POST.get('password')
        user = authenticate(request, index_number=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff and user.is_superuser:
                user.number_of_visits += 1
                return redirect('administration:dashboard')
            user.number_of_visits += 1
            return redirect('applicant:home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('accounts:login')


class SignUpView(View):
    template_name = "accounts/sign-up.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('accounts:login')
