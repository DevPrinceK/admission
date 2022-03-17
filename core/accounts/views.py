import re
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from applicant.models import Applicant


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
                user.save()
                return redirect('administration:dashboard')
            user.number_of_visits += 1
            user.save()
            return redirect('applicant:home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('accounts:login')


class SignUpView(View):
    template_name = "accounts/sign-up.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        index_number = request.POST.get('index_number')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('accounts:sign_up')
        user = Applicant.objects.create_applicant(
            index_number=index_number, password=password)
        user.save()
        messages.success(request, 'Account Created successfully!')
        login(request, user)
        user.number_of_visits += 1
        user.save()
        return redirect('applicant:home')


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('accounts:login')


class Error404View(View):
    template_name = 'accounts/404.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


class Error500View(View):
    template_name = 'accounts/500.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)
