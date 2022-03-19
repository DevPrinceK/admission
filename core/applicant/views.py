from django.db.models import Q
import uuid
import time
from email.mime import application
from uuid import uuid4
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from applicant.forms import BioForm
from django.utils.decorators import method_decorator
from applicant.models import Applicant, Transaction
from core.utils.decorators import AdminOnly, ApplicantsOnly
from administration.models import Admission
from django.http import HttpResponse
from core.utils.util_functions import html_to_pdf, make_payment, get_transaction_status
from core import settings


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


def generate_id():
    return int(time.time() * 1000)


# generate a uuid for the transaction


def generate_transaction_id():
    return str(uuid.uuid4())


class PaymentView(View):
    template_name = 'applicant/payment.html'

    @method_decorator(ApplicantsOnly)
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    @method_decorator(ApplicantsOnly)
    def post(self, request, *args, **kwargs):
        print('the payment is being processed')
        user = request.user
        phone = request.POST.get('phone')
        amount = request.POST.get('amount')
        network = request.POST.get('network')
        note = request.POST.get('note')
        transaction_id = generate_transaction_id()

        data = {
            'transaction_id': transaction_id,
            'mobile_number': phone,
            'amount': amount,
            'wallet_id': settings.WALLET_ID,
            'network_code': network,
            'note': note,
        }
        response = make_payment(data)
        # wait for 40 seconds for transaction to be processed
        for i in range(4):
            time.sleep(10)
            transaction_status = get_transaction_status(transaction_id)
            if transaction_status['success'] == True:
                print('the transaction was successful')
                user.has_paid = True
                break

        transaction = {
            'transaction_id': transaction_id,
            'amount': amount,
            'phone': phone,
            'network': network,
            'note': note,
            'status_code': transaction_status['status_code'],
            'status_message': transaction_status['message'],
            'applicant': user,
        }
        Transaction.objects.create(**transaction)
        return redirect('applicant:transactions')


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


class GeneratePDF(View):
    template_name = 'applicant/admission_letter.html'

    def get(self, request, *args, **kwargs):
        html = self.template_name
        admission = Admission.objects.filter(
            applicant=request.user, revoked=False).first()
        comtext = {
            'user': request.user,
            'admission': admission,
        }
        pdf = html_to_pdf(html, comtext)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = f'tashtech-admission-letter-{request.user.index_number}.pdf'
            content = f"attachment; filename={filename}"
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


class TransactionView(View):
    template_name = 'applicant/transactions.html'

    def get(self, request, *args, **kwargs):
        # transactions = request.user.transactions.all()
        transactions = Transaction.objects.filter(
            applicant=request.user).order_by('-date_created')
        context = {'transactions': transactions}
        return render(request, self.template_name, context)


class RecheckTransactionStatusView(View):
    template_name = 'applicant/recheck_status.html'

    def get(self, request, transaction_id, *args, **kwargs):
        transaction = Transaction.objects.get(transaction_id=transaction_id)
        response = get_transaction_status(transaction.transaction_id)
        transaction.status_code = response['status_code']
        transaction.status_message = response['message']
        messages.info(
            request, f'Rechecked status of transaction {transaction.transaction_id}! Updated status is {transaction.status_message}')
        return redirect('applicant:transactions')


class SearchTransactionView(View):
    template_name = 'applicant/transactions.html'

    def get(self, request, *args, **kwargs):
        query = request.GET.get('query')
        if query:
            transactions = Transaction.objects.filter(
                Q(transaction_id__icontains=query) |
                Q(phone__icontains=query) |
                Q(note__icontains=query) |
                Q(status_message__icontains=query) |
                Q(status_code__icontains=query)
            )
        else:
            transactions = Transaction.objects.filter(
                applicant=request.user).order_by('-date_created')
        context = {'transactions': transactions}
        return render(request, self.template_name, context)
