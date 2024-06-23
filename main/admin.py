from django.contrib import admin
from main.models import SharedText

# Register your models here.
class SharedTextAdmin(admin.ModelAdmin):
    list_display = ('title','note','slug', 'fileid', 'upload_time', 'expiration_time', 'is_expired')
    list_filter = ('upload_time', 'expiration_time')
    search_fields = ('title', 'slug', 'fileid')
    ordering = ('upload_time', 'expiration_time')

admin.site.register(SharedText,SharedTextAdmin)