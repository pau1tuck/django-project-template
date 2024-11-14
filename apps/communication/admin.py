# apps/communication/admin.py
from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    exclude = (
        "created_at",
        "modified_at",
    )
