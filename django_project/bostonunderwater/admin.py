from django.contrib import admin
from bostonunderwater.models import Totem, Node, Beacon
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    class Meta:
        model = Contact

admin.site.register(Totem)
admin.site.register(Node)
admin.site.register(Beacon)
admin.site.register(Contact, ContactAdmin)
