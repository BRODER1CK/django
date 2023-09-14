from django.contrib import admin

from .models import Choice, Question

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']

    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']})
    ]

    list_display = ('pub_date', 'question_text', 'was_published_recently')

    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)