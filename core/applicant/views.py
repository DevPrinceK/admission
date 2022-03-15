from django.shortcuts import render
from django.views import View


class HomepageView(View):
    template_name = 'applicant/homepage.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)

