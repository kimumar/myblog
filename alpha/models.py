from django.db import models
from django.forms import ModelForm
from django.forms import  TextInput, EmailInput, FileInput, Select
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Post(models.Model):
    CATEGORY = (
        ('Politics', 'Politics'),
        ('Tech', 'Tech'),
        ('Health', 'Health'),
        ('Product', 'Product'),
        ('Lifestyle', 'Lifestyle'),
        ('Quotes', 'Quotes'),
    )
    blog_image = models.ImageField(blank=True, null=True, upload_to='images/')
    date = models.CharField(blank=True, null=True, max_length=200)
    title = RichTextUploadingField(blank=True, null=True)
    post = RichTextUploadingField(blank=True, null=True)
    category = models.CharField(blank=True, null=True, max_length=200, choices=CATEGORY)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title or ""

    class Meta:
        ordering = ('-created',)


CATEGORY = (
        ('Politics', 'Politics'),
        ('Tech', 'Tech'),
        ('Health', 'Health'),
        ('Product', 'Product'),
        ('Lifestyle', 'Lifestyle'),
        ('Quotes', 'Quotes'),
    )

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'date', 'post', 'blog_image', 'category']

class CommentMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
    )

    post = models.ForeignKey('Post', on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80, blank=True, null=True)
    email = models.EmailField(max_length=80, blank=True, null=True)
    website = models.CharField(blank=True, null=True, max_length=200)
    message = models.TextField(blank=True, null=True, max_length=2000)
    status = models.CharField(blank=True, null=True, max_length=200, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)



class CommentForm(ModelForm):
    class Meta:
        model = CommentMessage
        fields = ['name', 'email', 'website', 'message']

class Sub(models.Model):
    email = models.CharField(blank=True, null=True, max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class SubForm(ModelForm):
    class Meta:
        model = Sub
        fields = ['email']

class ContactMessage(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    subject = models.CharField(blank=True, null=True, max_length=200)
    message = models.TextField(blank=True, null=True, max_length=2000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or ""



class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'subject', 'message']