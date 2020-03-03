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