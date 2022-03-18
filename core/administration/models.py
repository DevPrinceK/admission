from django.db import models

from applicant.models import Applicant


class Admission(models.Model):
    def generate_id():
        number = Admission.objects.count() + 1
        if number < 10:
            number = '00000' + str(number)
        elif number < 100:
            number = '0000' + str(number)
        elif number < 1000:
            number = '000' + str(number)
        return 'tsadm' + number

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


class Program(models.Model):
    def generate_id():
        number = Program.objects.count() + 1
        if number < 10:
            number = '00' + str(number)
            return 'tsprog' + number
        elif number < 100:
            number = '0' + str(number)
            return 'tsprog' + number

    program_code = models.CharField(max_length=10, default=generate_id)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.program_code
