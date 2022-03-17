from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from accounts.views import Error500View, Error404View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applicant.urls')),
    path('', include('accounts.urls')),
    path('administration/', include('administration.urls')),
]

# customised error handling page for errors 404 and 500
handler404 = Error404View.as_view()
handler500 = Error500View.as_view()
