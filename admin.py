from django.contrib import admin
from .models import Category, Product


@admin.action(description= 'return quantity to 0')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'quantity']
    ordering = ['category', '-quantity']
    list_filter = ['date_added', 'price']
    search_fields = ['description']
    search_help_text = 'Search Description'
    actions = [reset_quantity]
    # fields = ['name', 'description', 'category', 'date_added', 'rating']
    readonly_fields = ['date_added', 'rating']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'More',
            {
                'classes': ['collapse'],
                'description': 'Catogorey of Product and description',
                        'fields':['category', 'description'],
        },
        ),
        (
            'Finance',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Rate and other',
            {
                'description': 'Rate made automatically',
                                            'fields': ['rating', 'date_added'],
            }
        ),
    ]

    admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
