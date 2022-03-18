from django.urls import path
from .views import BioDataView, HomepageView, MyAdmissionView, PaymentView, BioSubmittedView, GeneratePDF

app_name = 'applicant'
urlpatterns = [
    path('home/', HomepageView.as_view(), name='home'),
    path('bio-data/', BioDataView.as_view(), name='bio_data'),
    path('bio-submitted/', BioSubmittedView.as_view(), name='submitted_bio'),
    path('payment/', PaymentView.as_view(), name='payment'),
    path('my-admission/', MyAdmissionView.as_view(), name='my_admission'),
    path('admission/', GeneratePDF.as_view(),
         name='download_admission_letter'),
]
