from unicodedata import name
from django.urls import path
from .views import DashboardView, AdmittedStudentView, ApplicantListView, StudentDetailView

app_name = 'administration'
urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('admitted/', AdmittedStudentView.as_view(), name='admitted'),
    path('applicants/', ApplicantListView.as_view(), name='applicants'),
    path('detail/<str:index_nuber>/', StudentDetailView.as_view(), name='student'),
    # path('login/', LoginView.as_view(), name='login'),
]
