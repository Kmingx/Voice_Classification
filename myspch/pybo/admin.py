from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Menu


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)


class MenuAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Menu, MenuAdmin)
