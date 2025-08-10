from django.contrib import admin
from .models import Category, Tag, Article, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'pub_date', 'is_published')
    list_filter = ('category', 'is_published', 'pub_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}  # توليد السلاج تلقائي من العنوان
    filter_horizontal = ('tags',)
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'article', 'created', 'active')
    list_filter = ('active', 'created')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
    approve_comments.short_description = "اعتماد التعليقات المحددة"
