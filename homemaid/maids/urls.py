from django.contrib import admin
from django.urls import path

from .views import MaidListView, maid_another_list_view


urlpatterns = [
    path('', MaidListView.as_view(), name='maid-list'),
    path('', maid_another_list_view, name='maid-another-list'),
]
