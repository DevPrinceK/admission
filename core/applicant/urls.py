from django.urls import path
from .views import BioDataView, HomepageView, MyAdmissionView, PaymentView, BioSubmittedView, GeneratePDF, TransactionView, RecheckTransactionStatusView, SearchTransactionView

app_name = 'applicant'
urlpatterns = [
    path('home/', HomepageView.as_view(), name='home'),
    path('bio-data/', BioDataView.as_view(), name='bio_data'),
    path('bio-submitted/', BioSubmittedView.as_view(), name='submitted_bio'),
    path('payment/', PaymentView.as_view(), name='payment'),
    path('my-admission/', MyAdmissionView.as_view(), name='my_admission'),
    path('admission/', GeneratePDF.as_view(),
         name='download_admission_letter'),
    path('transactions/', TransactionView.as_view(), name='transactions'),

    path('search-transactions/', SearchTransactionView.as_view(),
         name='search_transactions'),


    path('recheck-status/<int:transaction_id>/',
         RecheckTransactionStatusView.as_view(), name='recheck_status'),
]
