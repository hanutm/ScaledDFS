### File Server for storing files created by different clients


class fileServer():
	## Holds and shares files

	def GET():
		pass

	def POST():
		pass

	def DELETE():
		pass

	def HEAD():
		pass


def local_path():
	## Converts path of file to absolute path

	pass

def checkFile():
	## Checks validity of file and filepath

	pass

def isLocked():
	## Checks if file is locked
	
	pass

def initFileServer():
	## Initialises File Server
	
	pass

_config = { 'lockserver' : None,
	    'nameserver' : None,
	    'directories' : [],
	    'fsroot' : 'fs/',
	    'server' : None
	  }

## load config files from fileserver

initFileServer()
