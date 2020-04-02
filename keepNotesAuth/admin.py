from django.contrib import admin
from keepNotesAuth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

# Register your models here.

class MyAdmin(admin.ModelAdmin):
    menu_title = "Users"
    menu_group = "Staff"

class KeepNotesAuthUser(UserAdmin):

    readonly_fields = ('date_joined', 'last_login')
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password','username')}),
        (('Personal info'), {
         'fields': ('first_name', 'last_name', 'telephone')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                      'groups')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


admin.site.register(User, KeepNotesAuthUser)

