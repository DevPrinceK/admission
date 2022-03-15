from django.shortcuts import render
from django.views import View


class HomepageView(View):
    template_name = 'applicant/homepage.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class LoginView(View):
    template_name = "applicant/login.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


class SignUpView(View):
    template_name = "applicant/sign-up.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)
