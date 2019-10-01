from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

from chartapp.models import Product, Contact, ContactInteraction


class MyAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('My site admin')

    # Text to put in each page's <h1> (and above login form).
    site_header = ugettext_lazy('My administration')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('Site administration')

class ContactAdmin(admin.ModelAdmin):
    fields = ["last_name", "first_name"]
    list_display = ["last_name", "first_name", 'about', ]
    def response_change(self, request, obj):
        pass

class ContactInteractionAdmin(admin.ModelAdmin):
    list_display = ["id", "show_firm_url","name", "contact", "contacts"]
    list_filter = []
    search_fields = []
    list_editable = [ "name"]

    def show_firm_url(self, obj):
        return '<a href="%s%s">%s</a>' % ('http://url-to-prepend.com/', obj.url_field, obj.url_field)

    show_firm_url.allow_tags = True
    show_firm_url.short_description = 'Column description'


admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactInteraction, ContactInteractionAdmin)
admin.site.register(Product)
