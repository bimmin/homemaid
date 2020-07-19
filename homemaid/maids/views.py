from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from rest_framework.views import APIView
from rest_framework.response import Response

from .forms import MaidForm
from .models import Maid
from .serializer import MaidSerializer


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


class MaidAddView(View):
    template_name = 'maid_add.html'

    def get(self, request):
        form = MaidForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        # data = request.POST
        # Maid.objects.create(name=data['name'])

        send_mail(
            'Subject here',
            'Here is the message.',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )

        form = MaidForm(request.POST)
        if form.is_valid():
            form.save()

        return HttpResponse()


class MaidListAPIView(APIView):
    def get(self, request):
        maids = Maid.objects.all()
        serializer = MaidSerializer(maids, many=True)
        return Response(serializer.data)
