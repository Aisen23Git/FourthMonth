from django.contrib import admin
from posts.models import Post, Comment, Tag

"""настраивает админ-панель"""

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'rate', 'created_at')
    search_fields = ['title']
    list_display_links = ['id', 'title']
    list_filter = ['rate']
    list_editable = ['rate']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)