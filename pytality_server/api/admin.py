from django.contrib import admin

from pytality_server.api.models import Snippet


class SnippetAdmin(admin.ModelAdmin):
    pass


admin.site.register(Snippet, SnippetAdmin)
