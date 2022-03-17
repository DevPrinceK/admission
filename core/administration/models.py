from django.db import models

from applicant.models import Applicant


class Admission(models.Model):
    def generate_id():
        return 'tsadm' + str(Admission.objects.count())

    admission_number = models.CharField(max_length=15, default=generate_id)
    applicant = models.ForeignKey(
        Applicant, on_delete=models.CASCADE, related_name='admission_applicant')
    administrator = models.ForeignKey(
        Applicant, on_delete=models.CASCADE, related_name='admission_administrator')
    revoked = models.BooleanField(default=False)
    date_revoked = models.DateField(null=True, blank=True, auto_now=True)
    date_admitted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.admission_number
