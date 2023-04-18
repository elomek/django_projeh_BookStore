from django.contrib import admin
from .models import Book, Comment


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'text', 'datetime_created',)


# admin.site.register(Book)
admin.site.register(Comment, CommentAdmin)




