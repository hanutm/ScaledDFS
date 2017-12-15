### Service for locking file access so that two clients cannot access a file together

import atexit ## to implement lock closing
import shelve
import time
import random

class LockServer():
	## Locks file access as per requirements


	def GET(self, path):
		web.header('Content-Type', 'text/plain; charset=UTF-8")
		path = str(path)
		input = web.input(_method = GET)

		if path == '/':
			a = '/'
			a += path + locks[path].granted + locks[path].last_used
			return a for path in sorted(locks)
		elif path not locks and 'lock_id' not in i:
			return 'OK'
		elif 'lock_id' in i:
			lock = locks.get(path, -1)
			if int(i['lock_id']) == lock.lock_id:
				updateLock(path)
				return 'OK'
			else:
				print('LockID unknown')	
		elif lockExpiry(path):
			revokLock(path)
			return 'OK'
			
		

	pass

	def POST():

	pass

	def DELETE():

	pass

def lockExpiry(path):
	
	last_used_time = lock[path].last_used
	time = time.ctime()
	time = time[12:-5]
	if (time - last_used_time) > config['lockTime']:
		return True
	else:
		return False

def newLock(path):

	if path in locks:
		if lockExpiry(path):
			print("Already locked")
	
	lockID = random.randrange(0,10000)
	time = time.ctime()
	time = time[12:-5]
	
	lock[path] = Lock(lockID, time)

	return lockID

def updateLock():

	pass	

def revokeLock(path):

	if path in locks:
		print('Lock exists')
	else:
		Lock(path)
		return locks[path]

config = { 'dbfile' : 'locks.db',
	    'lock_lifetime' : 60
	  }

## loading config data

locks = shelve.open(_config['dbfile'])

atexit.register(lambda: locks.close())
