from django.contrib import admin
from .models import *


class BenefitsAdmin(admin.ModelAdmin):
    list_display = ('top_text', 'integer', 'bot_text', 'slug')


class MenuAdmin(admin.ModelAdmin):
    list_display = ('text', 'slug')
    prepopulated_fields = {'slug': ('text',)}


admin.site.register(Site)
admin.site.register(Benefits, BenefitsAdmin)
admin.site.register(Menu, MenuAdmin)
