### Service for locking file access so that two clients cannot access a file together

import atexit ## to implement lock closing
import shelve

class LockServer():
	## Locks file access as per requirements


	def GET():

	pass

	def POST():

	pass

	def DELETE():

	pass

def lockExpiry():

	pass

def newLock():

	pass

def checkNewLock():

	pass

def updateLock():

	pass

def revokeLock():

	pass


_config = { 'dbfile' : 'locks.db',
	    'lock_lifetime' : 60
	  }

## loading config data

_locks = shelve.open(_config['dbfile'])

atexit.register(lambda: _locks.close())
