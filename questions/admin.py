from django.contrib import admin
from .models import Question, Tag, Attempt

@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ("user", "question", "correct")

admin.site.register(Question)
admin.site.register(Tag)
