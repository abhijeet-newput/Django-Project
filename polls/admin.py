# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3


class QuestionAdmin(admin.ModelAdmin):
	fieldset : [ (None ,  {'fields' : ['question_text']}), ("Choices", {'fields' : ['question_text'], 'classes' : ['collapse']})]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

# Register your models here.
