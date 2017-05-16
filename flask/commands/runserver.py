#coding:utf8


from flask import Flask

from flask.create_app import FlaskApiResource


class Command(object):

	def handler(self):

		print 'i am runserver'
		# 第四个参数from_list，如果是空表示import settings 如果是[name1]意义就是from settings import name1...
		settings_module = __import__('settings', {}, {}, [])
		project_name = getattr(settings_module, 'PROJECT_NAME')
		DEBUG_MODEL = getattr(settings_module, 'DEBUG', False)
		HOST = getattr(settings_module, 'HOST', '127.0.0.1')
		PORT = int(getattr(settings_module, 'PORT', '5000'))
		# 加载所有的用户实现的middelwares
		__import__('middlware', {}, {}, ['*'])
		app = Flask(project_name)
		FlaskApiResource().init_app(app)

		app.run(debug=DEBUG_MODEL, host=HOST, port=PORT)
		# 处理route
		print 'starting...'
