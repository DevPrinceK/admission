from time import time
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser

from accounts.ApplicantManager import ApplicantManager
from core.utils.constants import (Programs, AdmissionStatus)


class Bio(models.Model):
    """
    Bio model
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    d_o_b = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    mother_name = models.CharField(max_length=255, null=True, blank=True)
    father_name = models.CharField(max_length=255, null=True, blank=True)
    guardian = models.CharField(max_length=255, null=True, blank=True)
    town = models.CharField(max_length=255, null=True, blank=True)

    first_choice = models.CharField(max_length=255)
    second_choice = models.CharField(max_length=255)

    jhs = models.CharField(max_length=255)
    year_of_completion = models.DateField()
    bece_aggregate = models.IntegerField(default=0)
    bece_results = models.FileField(
        upload_to='bece_results', null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_aggregate(self):
        return self.bece_aggregate

    def get_fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Applicant(AbstractBaseUser, PermissionsMixin):
    index_number = models.CharField(max_length=15, unique=True)
    bio = models.OneToOneField(Bio, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_applicant = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    is_admitted = models.BooleanField(default=False)
    admission_status = models.CharField(
        max_length=255, default=AdmissionStatus.PENDING.value)
    program_admitted_into = models.CharField(
        max_length=255, null=True, blank=True)

    number_of_visits = models.IntegerField(default=0)

    date_created = models.DateTimeField(auto_now_add=True)
    date_admitted = models.DateTimeField(null=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True)

    objects = ApplicantManager()

    USERNAME_FIELD = 'index_number'
    # REQUIRED_FIELDS = ['year']

    def __str__(self):
        return self.index_number


class Transaction(models.Model):
    def generate_id(self):
        return time() * 100000

    transaction_id = models.CharField(
        max_length=25, unique=True, default=generate_id)
    applicant = models.ForeignKey(
        Applicant, on_delete=models.CASCADE, related_name='payer')
    amount = models.IntegerField(default=0)
    network = models.CharField(max_length=15)
    note = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=15)
    status_code = models.CharField(max_length=5)
    status_message = models.CharField(max_length=255)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.transaction_id


# class Program(models.Model):

#     def generate_id(self):
#         prefix = str(self.name[:3].upper())
#         return prefix + str(time() * 1000)

#     name = models.CharField(max_length=255)
#     program_id = models.CharField(
#         max_length=255, unique=True, default=generate_id)

#     def __str__(self):
#         return self.name

# NOTE: THOIS FUNCTION IS REDUNDANT
class Program(models.Model):
    def generate_id():
        return 'tsprog' + str(Program.objects.count())
    name = models.CharField(max_length=100)

    # def generate_id():
    #     number = Program.objects.count() + 1
    #     prefix = str(Program.name[:3].upper())
    #     if number < 10:
    #         return prefix + '00' + str(number)
    #     elif number < 100:
    #         return prefix + '0' + str(number)

    program_code = models.CharField(max_length=10, default=generate_id)
