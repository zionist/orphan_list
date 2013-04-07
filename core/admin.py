from orphan_list.core.models.passport import Passport
from django.contrib import admin

class PassportAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'birthday', 'owner', 'may_edit')
    search_fields = ('owner', 'name', 'surname', 'birthday')
    list_filter = ('may_edit', )

admin.site.register(Passport, PassportAdmin)

