from django.urls import path

from administration.views import LoginView
from .views import HomepageView, LoginView, SignUpView


app_name = 'applicant'
urlpatterns = [
    path("login/", LoginView.as_view(), name='login'),
    path("sign-up/", SignUpView.as_view(), name='sign_up'),
    path('home/', HomepageView.as_view(), name='home'),

]
