from django.contrib import admin
from .models import BlogPage, BlogPagesAdmin, Categories, Tag

# Register your models here.

admin.site.register(BlogPage, BlogPagesAdmin)
admin.site.register(Categories)
admin.site.register(Tag)
