from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .models import Maid


class MaidListView(View):
    template_name = 'maid_list.html'

    def get(self, request):
        context = {
            'maid_list': Maid.objects.all()
        }
        return render(request, self.template_name, context)


def maid_another_list_view(request):
    template_name = 'maid_list.html'
    if request.method == 'GET':
        context = {
            'maid_list': Maid.objects.all()
        }
        return render(request, template_name, context)
