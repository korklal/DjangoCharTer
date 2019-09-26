from django.contrib import admin

from chartapp.models import Product, Contact


class ContactAdmin(admin.ModelAdmin):
    fields = ["last_name", "first_name"]


admin.site.register(Contact, ContactAdmin)
admin.site.register(Product)
