from django.contrib import admin
from .models import *
from django.utils.html import format_html


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('thumb', 'name', 'email', 'telephone')

    def thumb(self, obj):
        return format_html(f'<img src="{obj.game_img.url}" alt="" width="32px">')


admin.site.register(Customer, CustomerAdmin)
