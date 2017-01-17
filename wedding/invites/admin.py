from django.contrib import admin

from .models import Invite, Guest
# Register your models here.

class GuestInline(admin.TabularInline):
    model = Guest

class InviteAdmin(admin.ModelAdmin):
    inlines = [
        GuestInline
    ]
    def url(self, obj):
        if obj.id:
            link = '<a href="%s">%s</a>' % (obj.get_absolute_url(), obj.get_absolute_url())
            return link
    url.allow_tags = True

admin.site.register(Invite, InviteAdmin)
#admin.site.register(Guest, GuestAdmin)
