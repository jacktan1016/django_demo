#定义自己的中间件
def simple_middleware(get_response):
	# 初始化打印2次
	print("初始化-------")

	def middleware(request):
		print("处理对象请求之前-----")
		response = get_response(request)
		print("处理对象请求之后-------")
		return response
	return middleware