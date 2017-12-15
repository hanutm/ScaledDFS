## Utilities for parsing json, and other tasks to be carried out for every transaction

import json
import os

from contextlib import closing
from http.client import HTTPConnection


def load_config(config,path):
	## parse data from file and update config files

	if os.path.exists(path):
		with open(path) as f:
			data = json.loads(f.read())
			config.update(data)
	else return

def get_port(s):
	## return tuple of host, port

	host, port = s.split(':')
	return host, int(port)

def Locked(path, host, port,lockID):
	## Check if file is locked

	with closing(HTTPConnection(host, port)) as con:
		if lockID is not None:
			path += '?lock_id='
			path += lockID
	
		con.request('GET',path)

		r = con.getresponse()

	return r.status != 200


def LockFile(path, host, port):
	## Lock file

	with closing(HTTPConnection(host, port)) as con:
		con.request('POST',path)
		resp = con.getresponse()
		status = resp.status

		if status != 200:
			print('Cannot grant lock')

	lockID = resp.read()
	return lockID

def unLock(path, host, port, lockID):
	## Unlock file 
	with closing(HTTPConnection(host,port)) as con:
		con.request('DELETE', path + ('lock_id=') + int(lockID))
		resp = con.getresponse()
	
	if response.status != 200:
		print('Cannot revoke lock on file', path)

def getServer(path, host, port):
	## get server details
	with closing(HTTPConnection(host,port)) as con:
		con.request('GET', path)
		resp = con.getresponse()
		status, server = response.status, response.read()

	if status == 200:
		return server

	return None
