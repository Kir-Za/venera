from django.contrib import admin
from gird_blog.models import SiteInfo, Newslenta, Event, Article, Keywords

class NewslentaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'time')

class KeyInline(admin.TabularInline):
    model = Keywords.article.through
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    inlines = [KeyInline, ]

# Register your models here.
admin.site.register(SiteInfo)
admin.site.register(Event)
admin.site.register(Newslenta, NewslentaAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Keywords)