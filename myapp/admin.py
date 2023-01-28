from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Person

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ('Personal Info', {'fields': ('username', 'email', 'password',)}),
        (None, {'fields': ('is_active', 'is_admin',)}),
    )
    list_display = ('username', 'email', 'is_active',)
    serach_fields = ('username')
    list_filter = ()
    ordering = ()
    filter_horizontal = ()

admin.site.register([Person])
