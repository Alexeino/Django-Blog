from django.contrib import admin

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost

# Apply summernote to all TextField in model.
class BlogPostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    exclude = ('slug',)
    summernote_fields = ('content',)
    list_display = ('id','title','category','date_created','featured')
    list_display_links = ('id','title',)
    search_fields = ('title',)
    list_per_page = 25

admin.site.register(BlogPost, BlogPostAdmin)