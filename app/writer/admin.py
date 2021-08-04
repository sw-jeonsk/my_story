from django.contrib import admin
from django.contrib.auth.models import Group
from .forms import WriterCreationForm, CustomWriterChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Writer


class WriterAdmin(BaseUserAdmin):
    form = CustomWriterChangeForm
    add_form = WriterCreationForm

    list_display = ("email", "name", "is_superuser", "is_staff", "updated_at", "created_at")
    list_filter = ("is_superuser",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ["name"]}),
        ("etc info", {"fields": ["created_at", "updated_at"]}),
        ("Permissions", {"fields": ("is_superuser", "is_staff")}),
    )

    add_fieldsets = (
        (
            None,
            {"classes": ("wide",), "fields": ("email", "name", "password1", "password2")},
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ()


admin.site.register(Writer, WriterAdmin)
admin.site.unregister(Group)
