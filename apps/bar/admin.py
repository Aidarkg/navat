from django.contrib import admin
from .models import Syrup, Drinks, Tea, Coffee, Alcohol, Beer


class BaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'quantity', 'unit', 'updated_at')
    list_display_links = ('title',)
    list_editable = ('quantity', 'unit')
    ordering = ('-updated_at',)

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


class AlcoholAdmin(admin.ModelAdmin):
    list_display = ('title', 'quantity', 'unit', 'category', 'updated_at')
    list_display_links = ('title',)
    list_filter = ('category',)
    search_fields = ('title', 'category')
    list_editable = ('quantity', 'unit', 'category')
    ordering = ('-updated_at',)

    fields = ('title', 'quantity', 'unit', 'category', 'updated_at')
    readonly_fields = ('updated_at',)


class BeerAdmin(BaseAdmin):
    pass


admin.site.register(Syrup, SyrupAdmin)
admin.site.register(Drinks, DrinksAdmin)
admin.site.register(Tea, TeaAdmin)
admin.site.register(Coffee, CoffeeAdmin)
admin.site.register(Alcohol, AlcoholAdmin)
admin.site.register(Beer, BeerAdmin)
