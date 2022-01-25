from django.contrib import admin
from . models import Post, CommentMessage, Sub, ContactMessage
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post')
    list_filter = ('date', 'created')
    search_fields = ('title', 'date', 'post')

class CommentMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'post', 'created', 'active')
    list_filter = ('active', 'created')
    search_fields = ('name', 'email', 'message')
    actions = ['approve_comments']

class SubAdmin(admin.ModelAdmin):
    list_display = ('email',)
    
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Post, PostAdmin)
admin.site.register(CommentMessage, CommentMessageAdmin)
admin.site.register(Sub, SubAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
