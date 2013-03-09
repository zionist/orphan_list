from orphan_list.core.models.passport import Passport
from django.contrib import admin

class PassportAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'birthday')

admin.site.register(Passport, PassportAdmin)

