from django.contrib import admin

# Register your models here.
# admin.py

from django.contrib import admin
from .models import *
# admin.site.register(User)
admin.site.register(Note)
admin.site.register(PDFUpload)
admin.site.register(Subject)
admin.site.register(Note_2)
admin.site.register(Image)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_role', 'occupation', 'university', 'department', 'gender')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('user_role', 'occupation', 'university', 'department', 'gender')}),
    )
    list_display = ['username', 'email', 'user_role', 'occupation', 'university', 'department', 'gender']

admin.site.register(User, CustomUserAdmin)

