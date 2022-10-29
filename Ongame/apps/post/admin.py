from django.contrib import admin

from apps.post.models import Notice


# Register your models here.

class PostAdmin(admin.ModelAdmin):

    list_display = ('author', 'category', 'create_at')
    search_fields = ['author', 'category', 'create_at']

admin.site.register(Notice, PostAdmin)