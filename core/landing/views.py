from django.views import View
from django.shortcuts import render


class LandingView(View):
    template_name = 'landing.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
