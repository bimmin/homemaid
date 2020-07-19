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
    if request.method == 'GET':
        html = ''
        maids = Maid.objects.all()
        for maid in maids:
            html += f'<li>{maid.name}</li>'

        return HttpResponse(html)
