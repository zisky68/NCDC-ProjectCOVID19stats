import json

from django.http import HttpResponse
from django.shortcuts import resolve_url
from django.views import View
from django.views.generic import TemplateView

from NCDC.views.main import scrap_ncdc_website


def obj_dict(obj):
    return obj.__dict__


class IndexPage(TemplateView):
    template_name = 'site/index.html'

    def get_context_data(self, **kwargs):
        context_data = super(IndexPage, self).get_context_data(**kwargs)
        context_data['refetch_url'] = resolve_url('refetch')
        return context_data


class RefetchData(View):
    def get(self, request, *args, **kwargs):
        content = json.dumps(scrap_ncdc_website(), default=obj_dict)
        return HttpResponse(content, 'application/json', 200)
