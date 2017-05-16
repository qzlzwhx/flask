#coding:utf8


import api_service


class FlaskApiResource(object):

	def __init__(self):
		# 项目的目录必须是api
		from api.resources import *

	def init_app(self, app):

		routes = api_service.routes

		for key, route in routes.items():
			print key, route
			resource_app = route.get('cls')()
			app.route(key)(resource_app.handle)

