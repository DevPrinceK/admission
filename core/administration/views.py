from django.shortcuts import render
from django.views import View


class LoginView(View):
    template_name = "administration/login.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


class DashboardView(View):
    template_name = 'administration/dashboard.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class AdmittedStudentView(View):
    template_name = "administration/admitted.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


class ApplicantListView(View):
    template_name = "administration/applicants.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


class StudentDetailView(View):
    template_name = "administration/student_detail.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)
