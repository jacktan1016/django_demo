from django import template

# 注册
register = template.Library()

#使用注册装饰器
@register.filter
def multi(x):
	return x*x