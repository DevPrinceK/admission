from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from applicant.models import Applicant, Transaction
from core.utils.constants import AdmissionStatus


class DashboardView(View):
    template_name = 'administration/dashboard.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class AdmitStudentView(View):
    template_name = 'administration/admit_student.html'

    def get(self, request, index_number, *args, **kwargs):
        context = {
        }
        return render(request, self.template_name, context)

    def post(self, request, index_number, *args, **kwargs):
        student = Applicant.objects.filter(index_number=index_number).first()
        student.admission_status = AdmissionStatus.APPROVED.value
        student.is_admitted = True
        student.program_admitted_into = request.POST.get('program')
        student.save()
        messages.success(
            request, f'Student with Index {index_number} and name {student.bio.get_fullname}  admitted successfully')
        return redirect('administration:applicants')


class AdmitAllApplicantsView(View):
    # template_name = 'administration/admit_all_applicants.html'

    def get(self, request, *args, **kwargs):
        return redirect('administration:applicants')

    def post(self, request, *args, **kwargs):
        applicants = Applicant.objects.filter(is_admitted=False)
        for applicant in applicants:
            applicant.admission_status = AdmissionStatus.APPROVED.value
            applicant.is_admitted = True
            applicant.program_admitted_into = applicant.bio.first_choice
            applicant.save()
        messages.success(
            request, f'{applicants.count()} applicants admitted successfully')
        return redirect('administration:admitted')


class AdmittedStudentView(View):
    template_name = "administration/admitted.html"

    def get(self, request, *args, **kwargs):
        students = Applicant.objects.filter(
            is_admitted=True, admission_status=AdmissionStatus.APPROVED.value)
        context = {'students': students}
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


class TransactionsView(View):
    template_name = 'administration/transactions.html'

    def get(self, request, *args, **kwargs):
        transactions = Transaction.objects.all().order_by('-transaction_id')
        context = {'transactions': transactions}
        return render(request, self.template_name, context)


class RegisterAdminUserView(View):
    template_name = 'administration/register_admin.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        index_number = request.POST.get('index_number')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # if index_number already exists
        if Applicant.objects.filter(index_number=index_number).exists():
            messages.error(
                request, f'Index number {index_number} already exists')
            return redirect('administration:register_admin')
        #  if password and confirmatin password do not match
        if password != confirm_password:
            messages.error(
                request, 'Password and Confirm Password do not match')
            return redirect('administration:register_admin')

        user = Applicant.objects.create_superuser(
            index_number=index_number, password=password)
        user.save()
        messages.success(request, f'User {index_number} created successfully')
        return redirect('administration:register_admin')
