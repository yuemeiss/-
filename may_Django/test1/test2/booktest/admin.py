from django.contrib import admin
from .models import BookInfo,HeroInfo

#自定义后台管理显示的字段
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','title','pub_date']   #list_display表示显示那些属性 是这个类中的固定属性

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','hname','hgender','hcomment','hbook']

# Register your models here.
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
