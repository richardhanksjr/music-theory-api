from django.contrib import admin
from .models import Question, Tag, Attempt
from django.db.models import Avg

@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ("user", "question", "correct", "number_correct", 
                    "number_incorrect", "total_attempts", "percent_correct")
    list_filter = ("user", "question", "correct", "number_correct", 
                    "number_incorrect", "total_attempts")
    search_fields = ('user__username',)

    def percent_correct(self, obj):
        result = Attempt.objects.filter(user=obj.user).aggregate(Avg('number_correct'))
        return result['number_correct__avg']


admin.site.register(Question)
admin.site.register(Tag)
