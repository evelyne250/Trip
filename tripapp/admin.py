from django.contrib import admin
from .models import Entries
from tripapp.models import Account
from django.contrib.auth.admin import UserAdmin

class MyUserAdmin(UserAdmin):
    model = Account
    list_display = ()  # Contain only fields in your `custom-user-model`
    list_filter = ()  # Contain only fields in your `custom-user-model` intended for filtering. Do not include `groups`since you do not have it
    search_fields = ()  # Contain only fields in your `custom-user-model` intended for searching
    ordering = ()  # Contain only fields in your `custom-user-model` intended to ordering
    filter_horizontal = () # Leave it empty. You have neither `groups` or `user_permissions`
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('mobile',)}),
    )


admin.site.register(Account, MyUserAdmin)


admin.site.register(Entries)
# Register your models here.
