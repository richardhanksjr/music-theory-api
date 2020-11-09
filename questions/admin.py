from django.contrib import admin
from .models import Question, Tag, Attempt

@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ("user", "question", "correct")
    list_filter = ('user', 'question', 'correct')
    search_fields = ('user__username',)


admin.site.register(Question)
admin.site.register(Tag)
