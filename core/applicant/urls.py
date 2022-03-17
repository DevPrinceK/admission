from django.urls import path
from .views import BioDataView, HomepageView, PaymentView, BioSubmittedView

app_name = 'applicant'
urlpatterns = [
    path('home/', HomepageView.as_view(), name='home'),
    path('bio-data/', BioDataView.as_view(), name='bio_data'),
    path('bio-submitted/', BioSubmittedView.as_view(), name='submitted_bio'),
    path('payment/', PaymentView.as_view(), name='payment'),
]
