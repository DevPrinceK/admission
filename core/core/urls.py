from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applicant.urls')),
    path('', include('accounts.urls')),
    path('administration/', include('administration.urls')),

]
