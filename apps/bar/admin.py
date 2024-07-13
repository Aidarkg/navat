from django.contrib import admin
from .models import Syrup, Drinks, Tea, Coffee


class BaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'quantity', 'unit', 'updated_at')
    list_display_links = ('title',)
    list_filter = ('title', 'unit', 'updated_at')
    list_editable = ('quantity', 'unit')

    fields = ('title', 'quantity', 'unit', 'updated_at')
    readonly_fields = ('updated_at',)


class SyrupAdmin(BaseAdmin):
    pass


class DrinksAdmin(BaseAdmin):
    pass


class TeaAdmin(BaseAdmin):
    pass


class CoffeeAdmin(BaseAdmin):
    pass


admin.site.register(Syrup, SyrupAdmin)
admin.site.register(Drinks, DrinksAdmin)
admin.site.register(Tea, TeaAdmin)
admin.site.register(Coffee, CoffeeAdmin)
