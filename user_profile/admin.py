from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import User
from questions.models import Attempt as AttemptModel

from .models import UserProfile

class AttemptInline(admin.TabularInline):
    model = AttemptModel

class UserProfileInline(admin.TabularInline):
    model = UserProfile

class UserAdmin(DjangoUserAdmin):
    inlines = (UserProfileInline, AttemptInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)