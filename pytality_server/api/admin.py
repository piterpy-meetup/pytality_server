from django.contrib import admin

from pytality_server.api.models import Snippet


class SnippetAdmin(admin.ModelAdmin):
    list_display = ('task_title', 'time_to_solve',)


admin.site.register(Snippet, SnippetAdmin)
