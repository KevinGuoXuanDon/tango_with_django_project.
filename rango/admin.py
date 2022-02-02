from django.contrib import admin
from rango.models import Category, Page, UserProfile


# Register your models here.
# 注册到/admin页面中
class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'url')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


admin.site.register(UserProfile)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page,PageAdmin)
