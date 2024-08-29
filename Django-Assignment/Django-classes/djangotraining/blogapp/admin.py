from django.contrib import admin
from .models import Post, Tags, Category, Comment  # Correct import for Comment

class TagsAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'url': ('name',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'url': ('name',)}

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'published']
    prepopulated_fields = {'url': ('title',)}   


class commentAdmin(admin.ModelAdmin):
    list_display = ['name', 'approved', ]
    list_editable = ['approved']

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, commentAdmin)  # This should be the Comment from your models
