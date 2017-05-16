#coding:utf8

import sys


def load_my_flask_command(command):
	model_path = 'flask.commands.%s' % command
	try:
		command_module = __import__(model_path, {}, {}, ['*',])
	except:
		return None
	return command_module


def load_app_command(command):
	model_path = 'commands.%s' % command
	return __import__(model_path, {}, {}, ['*',])


def commands_excute(command):
	command_module = load_my_flask_command(command)
	if not command_module:
		command_module = load_app_command(command)
	print command_module
	if command_module:
		command_instance = getattr(command_module, 'Command')()
		command_instance.handler(*sys.argv[2:])
	else:
		print 'There are`t any commands!'
