from django.contrib import admin
from .models import ShiftLog

@admin.register(ShiftLog)
class ShiftLogAdmin(admin.ModelAdmin):
    list_display = ['engineer_name', 'shift_date', 'shift_type', 'created_at']
    search_fields = ['engineer_name', 'incidents']