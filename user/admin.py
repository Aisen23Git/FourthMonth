from django.contrib import admin
from user.models import Profile


@admin.site.register(Profile)
# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):