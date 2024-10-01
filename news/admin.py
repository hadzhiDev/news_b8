from django.contrib import admin

from news.models import News, Category, Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'date')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'content', 'description')
    list_filter = ('date', 'category')



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


# admin.site.register(News)
# admin.site.register(Category)
