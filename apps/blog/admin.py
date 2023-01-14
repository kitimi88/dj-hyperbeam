from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # fieldsets = (
    #     (None,{'fields':['title']}),
    #     ('Author',{'fields':['author']}),
    #     ('Slug',{'fields':['slug']}),
    #     ('Image',{'fields':['image']}),
    #     ('Body',{'fields':['body']}),
    #     ('Status',{'fields':['status']}),
    #     ('Tags',{'fields':['tags']}),
    # )
    list_display = ('title', 'author', 'publish', 'status','tag_list')
    list_filter = ('status', 'created', 'publish',  'author',)
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ("author",)
    date_hierarchy = 'publish'
    ordering = ('status',)
    # list_display = ['tag_list']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

