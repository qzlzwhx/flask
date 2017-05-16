# flask
#本项目是基于flask的<br>
名称引入未做任何修改，仍然是from flask import ***<br>

本文安装完以后主要做了修改。<br>
1.模拟django的中间件，允许用户可以自定义类似于django的middleware，实现process_request， process_respons<br>
（但是未实现从setting.py文件导入那种方式，这个很简单就暂时放下了）e。<br>
2.模拟django的python manager.py XXXX执行命令方式。用户可以自定义command。<br>
3.不在基于@route(func)方式引入路由，而是通过对象继承方式，实现路由，以方便restfull风格api设计。<br>

网上看到的很多关于flask的路由的源代码研究，讲真，底层都是套接字编程，framwork将uri映射到某个处理函数。flask也是使用python内置的SocketServer进行实现。<br>
其他的hack继续研究中。<br>
例子：<br>
middleware：<br>

from flask.middlewares.BaseMiddleware import BaseMiddleware<br>
class TestMiddleware(BaseMiddleware):<br>

	def request_process(self, req):
		print '-------------------'
		print req
		print '-------------------'

	def response_process(self, resp):
		print '================'
		print resp
		print '================'
		pass

command<br>
注意这个command需要在项目跟目录<br>
class Command(object):<br>

	def handler(self, *args):
		print 'love'
		print args

api：<br>
from flask.api_service import ApiService<br>


class Hello(ApiService):<br>
	app = 'hello'
	resource = ''

	def get(self):
		print 'hello do you love me '
		return 'this is my test'




