from django.contrib.auth.models import BaseUserManager


class ApplicantManager(BaseUserManager):
    '''Manages applicants creation'''

    def create_applicant(self, index_number, password, **kwargs):
        applicant = self.model(index_number=index_number,
                               password=password, **kwargs)
        applicant.set_password(password)
        applicant.save()
        return applicant

    def create_superuser(self, index_number, password, **kwargs):
        user = self.create_applicant(index_number=index_number,
                                     password=password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.is_applicant = False
        user.save()
        return user
