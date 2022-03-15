from django.urls import path

from .views import LoginView, SignUpView


app_name = 'accounts'
urlpatterns = [
    path("login/", LoginView.as_view(), name='login'),
    path("sign-up/", SignUpView.as_view(), name='sign_up'),
    path('logout/', LoginView.as_view(), name='logout'),
]
