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