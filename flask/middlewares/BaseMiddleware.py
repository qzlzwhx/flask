# -*- coding: utf-8 -*-


class BaseMiddleware(object):

	def request_process(self, req):
		pass

	def response_process(self, resp):
		pass
