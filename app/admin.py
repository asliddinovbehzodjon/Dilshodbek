from django.contrib import admin

# Register your models here.
from .models import Info
@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
     search_fields=['file_name','chat_id']
     list_display=['file_name','chat_id']