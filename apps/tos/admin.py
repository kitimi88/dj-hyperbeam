from django.contrib import admin
from .models import Policy

@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status','tag_list')
    list_filter = ('status', 'created', 'publish',  'author',)
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    
    #raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status',)
    # list_display = ['tag_list']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
