from django.contrib import admin
from .models import Poll, Choice, Vote

# @admin.register(Poll)
# class PollAdmin(admin.ModelAdmin):
#     list_display = ['title','author','publish','active']
#     search_fields = ['title','author__username']
#     list_filter = ['active']
#     date_hierarchy = 'publish'
#     prepopulated_fields = {'slug': ('title',)}

# @admin.register(Choice)
# class ChoiceAdmin(admin.ModelAdmin):
#     list_display = ['choice_text','poll']
#     search_fields = ['choice_text','poll__text']
#     autocomplete_fields = ['poll']


# @admin.register(Vote)
# class VoteAdmin(admin.ModelAdmin):
#     list_display = ['choice','poll']
#     search_fields = ['choice__choice_text','poll__text']
#     autocomplete_fields = ['choice','poll']

""""""
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),

        ('Author',               {'fields': ['author']}),
        ('Description', {'fields':['description']}),
        ('Date information', {'fields': ['publish']}),
        #('Choices', {'fields': ['choice_text']}),
    ]

    inlines = [ChoiceInline]
    list_display = ('title', 'publish','author','get_vote_count',)
    list_filter = ['publish']
    search_fields = ['title']
    


admin.site.register(Poll, PollAdmin)

