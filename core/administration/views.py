from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.utils.decorators import method_decorator

from applicant.models import Applicant, Transaction
from core.utils.constants import AdmissionStatus
from core.utils.decorators import AdminOnly, ApplicantsOnly


class DashboardView(View):
    template_name = 'administration/dashboard.html'

    @method_decorator(AdminOnly)
    def get(self, request):
        total_applicants = Applicant.objects.filter(is_applicant=True).count()
        total_transactions = Transaction.objects.count()
        total_administrators = Applicant.objects.filter(
            is_staff=True, is_superuser=True).count()

        total_admitted = Applicant.objects.filter(
            is_applicant=True, is_admitted=True,
            admission_status=AdmissionStatus.APPROVED.value).count()
        total_rejected = Applicant.objects.filter(
            is_applicant=True,
            admission_status=AdmissionStatus.REJECTED.value).count()
        total_pending = Applicant.objects.filter(
            is_applicant=True, admission_status=AdmissionStatus.PENDING.value).count()

        percentage_rejected = '0.00 %' if total_applicants == 0 else str(
            (total_rejected / total_applicants) * 100) + ' %'

        percentage_pending = '0.00 %' if total_applicants == 0 else str(
            (total_pending / total_applicants) * 100) + ' %'

        applicants_this_week = Applicant.objects.filter(is_applicant=True,
                                                        date_created__gte=datetime.now() - timedelta(days=7)).count()
        admitted_this_week = Applicant.objects.filter(
            admission_status=AdmissionStatus.APPROVED.value,
            date_admitted__gte=datetime.now() - timedelta(days=7)).count()

        percentage_admitted_this_week = '0.00 %' if applicants_this_week == 0 else str(
            (admitted_this_week / applicants_this_week) * 100) + ' %'

        percentage_of_applicants_this_week = '0.00 %' if total_applicants == 0 else str(
            (applicants_this_week / total_applicants) * 100) + ' %'

        total_visits = 0
        for user in Applicant.objects.all():
            total_visits += user.number_of_visits

        context = {
            'total_applicants': total_applicants,
            'total_transactions': total_transactions,
            'total_administrators': total_administrators,
            'total_admitted': total_admitted,
            'total_rejected': total_rejected,
            'total_pending': total_pending,
            'percentage_rejected': percentage_rejected,
            'applicants_this_week': applicants_this_week,
            'admitted_this_week': admitted_this_week,
            'percentage_pending': percentage_pending,
            'percentage_admitted_this_week': percentage_admitted_this_week,
            'percentage_of_applicants_this_week': percentage_of_applicants_this_week,
            'total_visits': total_visits
        }
        return render(request, self.template_name, context)


class AdmitStudentView(View):
    template_name = 'administration/admit_student.html'

    @method_decorator(AdminOnly)
    def get(self, request, index_number, *args, **kwargs):
        context = {
        }
        return render(request, self.template_name, context)

    @method_decorator(AdminOnly)
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

    @method_decorator(AdminOnly)
    def get(self, request, *args, **kwargs):
        return redirect('administration:applicants')

    @method_decorator(AdminOnly)
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

    @method_decorator(AdminOnly)
    def get(self, request, *args, **kwargs):
        students = Applicant.objects.filter(
            is_admitted=True, admission_status=AdmissionStatus.APPROVED.value)
        context = {'students': students}
        return render(request, self.template_name, context)


class ApplicantListView(View):
    template_name = "administration/applicants.html"

    @method_decorator(AdminOnly)
    def get(self, request, *args, **kwargs):
        applicants = Applicant.objects.filter(
            is_applicant=True).order_by('-date_created')
        context = {'applicants': applicants}
        return render(request, self.template_name, context)


class StudentDetailView(View):
    template_name = "administration/student_detail.html"

    @method_decorator(AdminOnly)
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


class TransactionsView(View):
    template_name = 'administration/transactions.html'

    @method_decorator(AdminOnly)
    def get(self, request, *args, **kwargs):
        transactions = Transaction.objects.all().order_by('-transaction_id')
        context = {'transactions': transactions}
        return render(request, self.template_name, context)


class RegisterAdminUserView(View):
    template_name = 'administration/register_admin.html'

    @method_decorator(AdminOnly)
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    @method_decorator(AdminOnly)
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
