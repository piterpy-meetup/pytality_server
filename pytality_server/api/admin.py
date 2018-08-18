from django.contrib import admin

from pytality_server.api.models import Snippet


class SnippetAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_title', 'time_to_solve',)
    list_display_links = ('id', 'task_title')


admin.site.register(Snippet, SnippetAdmin)
