from django.contrib import admin
from .models import Program


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("description", "duration_days",  "price", "display_order", "active")
    # list_filter = ("user",)
