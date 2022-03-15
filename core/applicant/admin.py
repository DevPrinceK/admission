from django.contrib import admin

from .models import Applicant, Bio, Transaction

admin.site.register(Applicant)
admin.site.register(Bio)
admin.site.register(Transaction)
