from django.contrib import admin
from .models import *
# from .models import Snippet
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .models import CustomUser
admin.site.site_header = 'Trip Dashboard'

class SnippetAdmin(admin.ModelAdmin):
   list_display = ('name','current location','destination','phone number', 'created')

# admin.site.register(Clients)
admin.site.register(Client)
admin.site.register(Entries)
admin.site.unregister(Group)

# Register your models here.

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username', 'name']

# admin.site.register(CustomUser, CustomUserAdmin)