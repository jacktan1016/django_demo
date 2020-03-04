第一天:
1、创建应用模块--->settings里注册应用
2、前端发送请求-->解析url--->路由(总路由里面设置子视图url(r'^auser/',include('auser.urls')))
   ----->子路由设置应用(url(r'^index/',views.index))---->view再返回html
核心:
1、客户端request发送请求
2、解析url
3、路由
4、Views返回结果

配置静态文件:
# 静态文件
STATIC_URL = '/static/'  (路径里面一定要有static，一定要通过它)
STATICFILES_DIRS=[os.path.join(BASE_DIR,"static_files")]

路由的屏蔽需要有头有尾 url(r"^login/$",views.login)  只在应用模块写$,不在总应用写/auser写$，因为这样写会写死url！

路由的反向解析：
根据视图函数，借用reverse，倒着推路由的路径
1、总urls:  namespace=""
2、子urls:  name=""
两种写法:
有namespace reverse('namespace:login')
没有namespace  reverse('login')

--------------------------------------------------------------------------------

第二天:
request对象:
1、请求时路径为/2008/beijing
url(r'^login/(\d+)/([a-zA-Z]+)',views.login)

为参数指定名字?P<>
url(r'^login/(?P<year>\d+)/(?P<city>[a-zA-Z]+)',views.login)

获取参数
login(request,year,city):
	print("year:",year)

2、请求时路径为?a=10&b=20&a=30
url(r'^login_query/',views.login_query)
def login_query(request):
	 data = request.GET()  # 这里的GET不是方法是，是获取参数的属性的意思
	 print(type(data))  # 类型是QueryDict类型，不是一个字典，因为它可以一键多值！
	 print(data.get('b'))
	 print(data.getlist('a')) # 多个值的话，必须得用getlist获取a的键是列表
	 return HttpResponse(".......")

3、请求体为form表单时
url(r'^login_form/',views.login_query)
def login_form(request):
	 data = request.POST()  # 这里的POST，能识别和获取的是form提交的参数
	 print(type(data))  # 类型是QueryDict类型，不是一个字典，因为它也可以一键多值！
	 print(data.get('b'))
	 print(data.getlist('a')) # 多个值的话，必须得用getlist获取a的键是列表
	 return HttpResponse(".......")
 记住在Post，路径写的时候一定要http://127.0.0.1:8000/brequest/login_form/，一定要写最好的/,因为你url匹配的时候有/
 form 表单里方式有post,delete,put,patch

 4、非form表单数据，text,json,html,xml
 def login_not_form(request):
 	 data = request.body # 这里是非表单
 	 print(type(data))  # 接收到的是一个二进制 byte 需要转换类型
 	 # 先转换为字符串类型后再转换为字典
 	 str_data = data.decode('gbk')  # windows里面默认decode为gbk
 	 dict_data = json.loads(data)  # 转换为字典
 	 return HttpResponse(dict_data)

 5、请求头meta
 def login_meta(request):
 	data = request.META   
 	print(type(data)) # 类型为字典，请求头相关信息是以键值对方式体现
 	print(data['content-Type'])
 	# 其他获取方法
 	print(request.method)  #请求方法
 	print(request.path)		# 请求路径，相当于reverse('')
 	return HttpResponse("....")

6、HttpResponse对象
def response_msg(request):
	#return HttpResponse(content="响应信息",content_type="返回的类型",status=200) # 3个参数

	response = HttpResponse()
	response.content="操作响应属性"
	response.status_code=200    # 注意这里是status_code和上面的默认形参不一样
	return response

7、jsonresponse对象
JsonResponse做了2件事情:
1、content_type="application/json"
2、content="" 为字符串类型
def jsonresponse(request):
	data = {"a":1,"b":2}
	return JsonResponse(data)

	# json 格式也有可能为数组
	data_1 = [{"a":1,"b":2}]
	return JsonResponse(data_1,safe = False)  # 如果想传数组，则将safe参数打开，给它传个False

8、重定向redirect

def response_redirect(request):
	 #定向自己的
	# /auser/login 注意最前面一定要有/，因为它会拼接为127.0.0.1auser,所以一定要/
	return redirect('/auser/login') 

	# 或者用reverse('')
	return redirect(reverse(''))

	#定向到其他域名
	return redict('http://www.baidu.com')

9、操作cookie   set_cookie和COOKIES  设置和取
def cookie(request):
	response = HttpResponse("操作cookie")
	# 设置cookie
	response.set_cookie('itcast','tanwen',max_age=30)  # key,value,max_age表示有效时间

	# 获取cookie
	cookie = request.COOKIES
	print(cookie)  # 字典类型
	return response
cookie:
1、身份识别
2、有限制4K大小
3、保持会话

10、session
 1、session共享:
  用户去各个应用模块时(分布式不同服务器)，去redis里去找sessionid，判断状态
 2、依赖cookie(不同的用户有不同的会话)
 session的配置
 redis :
 select 1  # 切换到1数据库
 # 设置session
 request.session['name'] = 'ttt'
 # 获取session
 print(request.session['name'])
 #删除session
 1 删除指定键和值
 del request.session['name']
 2 删除所有的键和值
 request.session.clear()
 3 删除整条数据
 request.session.flush()

 浏览器--->服务器,服务器会生成自己命名客户的session键值对，存储在redis，同时会给客户端一个随机码。
 在redis里面，键是django框架set名字和随机码组合。电脑上设置的值只是redis值得一部分
 这里有个Bug ：取消redis的登录验证，不然django会报错，权限校验！
 redis里的key :1:django.contrib.sessions.cachewpjutnv42gnniisfqy1uxtv4hg2sj5x4
 对应的value:"\x80\x04\x95\x14\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x04name\x94\x8c\x06tanwen\x94s."

 ---------------------------------------------------------------------------------------------
 类视图:
 1、views里面
 class LoginView(View):   #继承View
 	def get(self,get):
 		return HttpResponse("类视图---get方法")
	def post(self,post):
		return HttpResponse("类视图---post方法")
def index(request):
	return HttpResponse(".....")

# LoginView.as_view()=index
url(r'^index/$',views.LoginView.as_view(),name='index')

>>> from django.http.request import HttpRequest
>>> from django.http.response import HttpResponse
>>> from ccookie.views import LoginView
>>> login_object = LoginView()
>>> request = HttpRequest()
>>> request.method='get'
>>> login_method = getattr(login_object,request.method)
>>> login_method
<bound method LoginView.get of <ccookie.views.LoginView object at 0x0000020A9B040888>>
>>> login_method(request)
<HttpResponse status_code=200, "text/html; charset=utf-8">
>>> response = login_method(request)
>>> response.content.decode('utf-8')
'类视图----get方法'

2、类视图使用装饰器
第一种:
装饰器里的wrapper方法添加self，然后将装饰器放在类的方法上面
第二种:
装饰器直接装饰url中的LoginView.as_view(),因为这返回的是一个方法，可以直接装饰
第三种
利用django框架的装饰器，就可以对类视图直接使用装饰器
#my_decorator是自己定义的装饰器,dispatch是原始代码中获取的请求方法
@method_decorator(my_decorator,name='dispatch')  

3、类视图添加扩展类Mixin
Mixin扩展多继承原理
class DecoratorMixin:
	@classmethod
	def as_view(cls,*args,**kwargs):
		# 这里是没有as_view()
		view = super().as_view(*args,**kwargs)
		view = my_decorator(view)
		return view

# 利用多继承的方法将View的as_view()方法给DecoratorMixin类里的方法，这是一种思想
class LoginView_Decorator_MiXin(DecoratorMixin,View):
	def get(self,get):
		return HttpResponse("类视图--DecoratorMixin--get方法")
	def post(self,post):
		return HttpResponse("类视图--DecoratorMixin--post方法")

4、中间件：提供共性功能
#定义自己的中间件，参数都是写死的,get_response,和request
def simple_middleware(get_response):
	# 初始化打印2次
	print("初始化-------")

	def middleware(request):
		print("处理对象请求之前-----")
		response = get_response(request)
		print("处理对象请求之后-------")
		return response
	return middleware
中间件写完之后，需要在settings里面去注册

在请求视图被处理前，中间件由上至下依次执行
在请求视图被处理后，中间件由下至上依次执行

5、django自带模板
1、创建templates文件夹
2、settings.py里面在列表里面加入

要返回html，需要用到render(request,htmlname,context) #context必须是字典
模板小结:
1、views里的render给前端传递的参数必须是 context = 字典,context为上下文的意思
2、html里直接调用字典里的键名，就可以调用值了，如:  {{ name }}
3、如果传来的context里的一个键对应的值是列表或者是字典，我们不能用sons[0]或者wife['name']
	一律用sons.或者wife.name去获取值
4、语法的格式，没有冒号,只有一个{},并且必须加%，而且要有结束语，如
{% for i in sons %}
{% empty %}
	<h2>如果列表不存在就不执行</h2>
{{forloop.counter }}  从1开始   {{forloop.counter0 }}  从0开始
{% endfor %}
最重要一点，>,<,=类似左右两边必须空格

6、django自带模板过滤器
{{ names | default:"没有值就是为false"}}
{{ sons | length }}
{{ date_time | date:"Y-m-d"}}

{{ data | safe }}    "data":"<ahref='http://www.baidu.com'>百度链接</a>"可以在前端展示为一个链接，否则是一个字符串

6、自定义模板文件
  1、在模块中创建一个package包，包名叫templatetags,然后新建py文件
  2、py文件中自己定义一个过滤方法，但是必须注册
  3、html中加载{% load oddfilter %}

7、继承模板
	子模板的内容
	{% extends "father.html" %}
	{% block ttt %}
	{{ block.super }}
	{% endblock ttt %}

--------------------------------------------------------------------------------------------
数据库：增删改查
配置数据库：
1、项目文件得init里面配置mysql，使得项目开始时就读取mysql
2、setting里设置mysql账户密码，和哪个数据库
3、mysql创建数据库

枚举
GENDER_CHOICES = (
        (0, 'female'),
        (1, 'male')
    )
hgender = models.SmallIntegerFiled(choices = GENDER_CHOICES,default=0,verbose_name="性别")
# 关联外键                                         级联操作
hbook = models.ForeignKey(BookInfo,on_delete=models.CASCADE,verbose_name="图书")

增加:
b =BookInfo()
b.btitle="xx"
b.pub_date = date(1990,1,1)
b.save()
删除:(首先要找到删哪个)
b = BookInfo.objects.get(id=1)
b.delete()
修改:(首先要找到修改哪个)
b = BookInfo.objects.get(id=1)
b.btitle= "hah"
b.save()

查询:
1、基本查询 get all count
2、过滤查询
	filter  得到的结果个列表
	BookInfo.objects.filter(id=1)
	取反
	BookInfo.objects.exlude(id=1)
	大于 gt，小于lt
	BookInfo.objects.filter(id__gt=1)  # 想要过滤，肯定要知道凭什么东西过滤--字段，过滤条件__
	大于等于gte，小于等于lte   (equal)
	在什么范围内
	BookInfo.objects.filter(id__in=[1,3,5])  # id 在1，3，5中查询
	包含什么
	BookInfo.objects.filter(id__contains='天龙')
	开始
	BookInfo.objects.filter(btitle__startswith="天")
	结尾
	BookInfo.objects.filter(btitle__endswith="部")
	空查询
	BookInfo.objects.filter(btitle__isnull=False)
	日期查询
	BookInfo.objects.filter(bpub_date__year=1991)
	BookInfo.objects.filter(bpub_date__gt=date(1991,1,1))

查询为属性和属性之间对比，或者多个组合查询时
1、导包
2、属性和属性之间对比
	BookInfo.objects.filter(bread__gt=F('bcomment'))
	BookInfo.objects.filter(bread__gt=F(bcomment)*2)  # 还可以用算法比较
3、多个条件组合
	BookInfo.objects.filter(btitle__gt=1,bread__gt=10) # 默认就为与得关系
	BookInfo.objects.filter(Q(btitle__gt=1) | Q(bread__gt=10))  # 或得关系

聚合查询和排序:
聚合查询
使用aggregate()过滤器调用聚合函数--合函数包括：Avg 平均，Count 数量，Max 最大，Min 最小，Sum 求和
BookInfo.objects.aggregate(Sum('id'))  
排序 
BookInfo.objects.all().order_by('bread')

关联查询
# 一本书里对应得英雄
book = BookInfo.objects.get(id=1)
book.heroinfo_set.all()     # 类小写_set.all()  all是一般查询
# 英雄对应数据
hero = HeroInfo.objects.get(id=2)
hero.hbook      #hbook是关联外键得键，这里直接写就可以知道书名了
hero.hbook_id   # 这里是得到Id，在通过id找书名，需要2步

关联过滤查询
# 查谁谁在前面，并且如果类中有外键就写外键，没外键就写对应类名
# 查询书名为“天龙八部”的所有英雄。
HeroInfo.objects.filter(hbook__btitle="天龙八部")
# 查询图书阅读量大于30的所有英雄
HeroInfo.objects.filter(hbook__bread__gt=30)
# 查询图书，要求图书英雄为"孙悟空"
BookInfo.objects.filter(heroinfo__hname="孙悟空")
# 查询图书，要求图书中英雄的描述包含"八"
BookInfo.objects.filter(heroinfo__hname__contains="八")

自定义管理器
1、不爽就重写它的方法
2、添加新的功能
首先在modles里面定义管理器类
class BookManager(models.Manager):  #继承的是models.Manager
	def add_book(self,title,date):
	 	book = BookInfo()
        book.btitle = title
        book.bpub_date = date
        book.save()
        return book
class BookInfo(models.Model): # 继承的是models.Model
	books = BookManager()		# 通过books = BookManager() 让两者之间产生关系

shell里面 BookInfo.books.add_book("ss",date(1991,2,2))


admin
账户和密码
admin   admin123
admin注册  ： admin.site.register(HeroInfo) 注册模块


关联对象

# 上传图片
1、下包
2、image字段
3、上传图片会上传到服务器，数据库存着的是图片路径