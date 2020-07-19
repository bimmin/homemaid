from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .models import Maid


class MaidListView(View):
    def get(self, request):
        # html = ''
        # maids = Maid.objects.all()
        # for maid in maids:
        #     html += f'<li>{maid.name}</li>'

        # return HttpResponse(html)

        maid_list = []
        maids = Maid.objects.all()
        for maid in maids:
            maid_list.append(maid.name)

        template_name = 'maid_list.html'
        context = {
            'maid_list': maid_list
        }
        return render(request, template_name, context)


def maid_another_list_view(request):
    if request.method == 'GET':
        html = ''
        maids = Maid.objects.all()
        for maid in maids:
            html += f'<li>{maid.name}</li>'

        return HttpResponse(html)
