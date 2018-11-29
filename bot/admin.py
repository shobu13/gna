from django.contrib import admin

from bot.models import *


class RoleAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_default')


admin.site.register(WordBlackList)
admin.site.register(Role, RoleAdmin)
