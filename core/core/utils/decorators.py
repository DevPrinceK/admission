from django.shortcuts import redirect


class AdminOnly(object):
    def __init__(self, original_method):
        self.original_method = original_method

    def __call__(self, request, *args,  **kwargs):
        if request.user.is_authenticated and request.user.is_superuser and request.user.is_staff:
            return self.original_method(request, *args, **kwargs)
        return redirect('accounts:login')


class ApplicantsOnly(object):
    def __init__(self, original_method):
        self.original_method = original_method

    def __call__(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_applicant:
            return self.original_method(request, *args, **kwargs)
        return redirect('accounts:login')
