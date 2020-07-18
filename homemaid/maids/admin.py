from django.contrib import admin

from .models import Maid


@admin.register(Maid)
class MaidAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'birthdate',
        'description',
        'cartificate',
        'salary',
    )
