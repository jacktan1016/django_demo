from django.contrib import admin
from dtemplates.models import BookInfo,HeroInfo

# Register your models here.

# 表格形式的展示
class HeroInfoTabularInline(admin.TabularInline):
    model = HeroInfo
    # 编辑的个数
    extra = 1

# 自定义admin管理器
class BookInfoAdmin(admin.ModelAdmin):
	# 列操作

	# 1、显示哪些字段
	list_display = ['id','btitle','bpub_date','date_time'] # date_time为自定义的
	# 2、每页显示的个数默认100
	list_per_page = 2
	# 3、操作选项的位置
	actions_on_top = True
	# 5、搜索框
	search_fields=['btitle']
	

	# 编辑页--详情页
	# 显示字段
	# fields = ['btitle','bpub_date']

	#分组显示
	fieldsets=(
	    ('必选',{'fields':('btitle','bpub_date','image')}),
	    ('选填',{'fields':('bread','bcomment'),'classes':('collapse',)}),
	)
	# 关联对象--块和表
	inlines = [HeroInfoTabularInline]



class HeroInfoAdmin(admin.ModelAdmin):
	list_display = ['id','hname','hbook','bread']  # bread 是自定义的
	# 4、右侧过滤器
	list_filter = ['hgender']
   


 
# 多继承
admin.site.register(BookInfo,BookInfoAdmin)

admin.site.register(HeroInfo,HeroInfoAdmin)



admin.site.site_header = '传智书城'
admin.site.site_title='传智书城MIS'
admin.site.index_title = '欢迎'