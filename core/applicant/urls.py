from django.urls import path
from .views import HomepageView

app_name = 'applicant'
urlpatterns = [
    path('home/', HomepageView.as_view(), name='home'),
]
