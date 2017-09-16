from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.utils.translation import ugettext as _


class LandingView(View):
    template_name = 'landing.html'
    translate = _("abc")

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
