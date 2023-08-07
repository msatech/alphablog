from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.register(Category)

admin.site.register(Comments)
admin.site.register(CommentReply)

@admin.register(Keywords)
class KeywordsAdmin(ImportExportModelAdmin):
    pass

@admin.register(Blogs)
class BlogsAdmin(ImportExportModelAdmin):
    pass


