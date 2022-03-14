from django.contrib.auth.models import BaseUserManager


class ApplicantManager(BaseUserManager):
    '''Manages applicants creation'''

    def create_applicant(self, index_number, year, **kwargs):
        applicant = self.model(index_number=index_number password=year, **kwargs)
        applicant.set_password(year)
        applicant.save()
        return applicant

    # def create_superuser(self, email, name, password, **kwargs):
    #     user = self.create_user(email, name,  password, **kwargs)
    #     user.is_superuser = True
    #     user.is_staff = True
    #     user.save()
    #     return user
