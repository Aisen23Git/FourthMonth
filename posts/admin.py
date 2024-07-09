from django.contrib import admin
from posts.models import Post

"""настраивает админ-панель"""

admin.site.register(Post)
