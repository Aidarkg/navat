from django.contrib import admin
from .models import Syrup


class SyrupAdmin(admin.ModelAdmin):
    list_display = ('title', 'quantity', 'unit', 'updated_at')
    list_display_links = ('title',)
    list_filter = ('title', 'unit', 'updated_at')
    list_editable = ('quantity', 'unit')

    fields = ('title', 'quantity', 'unit', 'updated_at')
    readonly_fields = ('updated_at',)


admin.site.register(Syrup, SyrupAdmin)
