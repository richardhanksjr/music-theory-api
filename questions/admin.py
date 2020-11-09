from django.contrib import admin
from .models import Question, Tag, Attempt

@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ("user", "question", "correct", "number_correct", 
                    "number_incorrect", "total_attempts")
    list_filter = ("user", "question", "correct", "number_correct", 
                    "number_incorrect", "total_attempts")
    search_fields = ('user__username',)


admin.site.register(Question)
admin.site.register(Tag)
