from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Comment, Tag

# admin.site.register(Post)

# class PostAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Post, PostAdmin)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'message', 'is_public',
                    'message_length', 'created_at', 'updated_at']
    list_display_links = ['photo_tag', 'message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']

    def message_length(self, post):
        return f"{len(post.message)} 글자"

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width:72px" />')
        return None

    # def is_public(self):
    #     return "공개   여부"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
