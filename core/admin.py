import reversion
from orphan_list.core.models.passport import Passport
from django.contrib import admin

class PassportAdmin(reversion.VersionAdmin):
    list_display = ('__unicode__', 'birthday', 'owner')
    search_fields = ('owner', 'name', 'surname', 'birthday')

admin.site.register(Passport, PassportAdmin)

