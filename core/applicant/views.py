from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from applicant.forms import BioForm
from django.utils.decorators import method_decorator
from core.utils.decorators import AdminOnly, ApplicantsOnly
from administration.models import Admission


class HomepageView(View):
    template_name = 'applicant/home.html'

    @method_decorator(ApplicantsOnly)
    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class BioDataView(View):
    template_name = 'applicant/bio.html'

    @method_decorator(ApplicantsOnly)
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    @method_decorator(ApplicantsOnly)
    def post(self, request, *args, **kwargs):
        bio_form = BioForm(request.POST, request.FILES or None)
        if bio_form.is_valid():
            print('the form is valid')
            bio_form.save()
            print('the form is saved')
            user = request.user
            user.bio = bio_form.instance
            user.save()
            print('the form is assigned to a user')
            messages.success(request, 'Bio data saved successfully')
            return redirect('applicant:submitted_bio')
        else:
            print('the form is not valid')
            messages.error(request, bio_form.errors)
            return redirect('applicant:bio_data')


class PaymentView(View):
    template_name = 'applicant/payment.html'

    @method_decorator(ApplicantsOnly)
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    @method_decorator(ApplicantsOnly)
    def post(self, request, *args, **kwargs):
        return redirect('applicant:submitted_payment')


class BioSubmittedView(View):
    template_name = 'applicant/bio_submitted.html'

    @method_decorator(ApplicantsOnly)
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    @method_decorator(ApplicantsOnly)
    def post(self, request, *args, **kwargs):
        template_name = 'applicant/payment.html'
        index_number = request.user.index_number
        context = {'index_number': index_number}
        return render(request, template_name, context)


class MyAdmissionView(View):
    template_name = 'applicant/my_admission.html'

    @method_decorator(ApplicantsOnly)
    def get(self, request, *args, **kwargs):
        admissions = Admission.objects.filter(
            applicant=request.user, revoked=False)
        context = {'admissions': admissions}
        return render(request, self.template_name, context)
