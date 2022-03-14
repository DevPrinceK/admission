from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser

from .ApplicantManager import ApplicantManager


class Bio(models.Model):
    """
    Bio model
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    age = models.IntegerField(default=0)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255)

    mother_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    guardian = models.CharField(max_length=255)
    town = models.CharField(max_length=255)

    fist_choice = models.CharField(max_length=255)
    second_choice = models.CharField(max_length=255)

    jhs = models.CharField(max_length=255)
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
    year = models.DateField()
    bio = models.OneToOneField(Bio, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_labourer = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    objects = ApplicantManager()

    USERNAME_FIELD = 'index_number'
    REQUIRED_FIELDS = ['year']

    def __str__(self):
        return self.index_number
