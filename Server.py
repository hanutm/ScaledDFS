### File Server for storing files created by different clients

''' to add, exceptional handling '''

import time
import os.path

from contextlib import closing
from http.client import HTTPConnection

import utils
import web

class fileServer():
	## Holds and shares files

	def GET():
		web.header('Content-Type', 'text/plain; charset=UTF-8')
		path = local_path(path)
		web.header('Last-Modified', time.ctime())
		with open(path) as f:
			return f.read()

	def POST():
		path = local_path(path)
		
		with open(path, 'w') as f:
			f.write(web.data())
	
		web.header('Last-Modified', time.ctime())

	def DELETE():

		web.header('Content-Type', 'text/plain; charset=UTF-8')

		os.unlink(local_path(path))
		return 'OK'

	def HEAD():
	
		web.header('Content-Type', 'text/plain; charset=UTF-8')

		path = local_path(path)
		web.header('Last-Modified', time.ctime())
		return ''


def local_path():
	## Converts path of file to absolute path
	return os.path.join(os.getcwd(), config['fsroot'], filepath[1:])
	

def checkFile():
	## Checks validity of file and filepath

	pass

def isLocked():
	## Checks if file is locked
	
	pass

def initFileServer():
	## Initialises File Server
	host, port = utils.get_port(config['nameserver'])
	with closing(HTTPConnection(host, port)) as con:
		data = 'srv='
		data += config['server']
		data += '&dirs='
		data += '/n'
		data += 'config['directories']'
		con.request('POST','/',data)

config = { 'lockserver' : None,
	    'nameserver' : None,
	    'directories' : [],
	    'fsroot' : 'fs/',
	    'server' : None
	  }

## load config files from fileserver

initfileServer()
