### Client side files for each client to Read/Write and modifying files present on the file server

from tempfile import SpooledTemporaryFile
import utils

def Delete(path, lockID = None):
	
	pass

class File(SpooledTemporaryFile):
	## Inspect file, its size, store in memory or disk depending on size

	def __init__(self, path, mode = 'rtc'):
		
		self.mode = mode
		self.path = path
		host,port = utils.get_port(_config['nameserver'])
		self.server = utils.getServer(path, host, port)
	
		if self.server is None:
			print('File not found')

		self.modified = None 


		SpooledTemporaryFile.__init__(self, _config['max_size'], mode.replace('c',''))		

		host,port = utils.get_port(_config['lockserver'])
		if utils.Locked(path, host, port):
			print('File is locked')	
	
		if 'w' not in mode:
			host, port = utils.get_port(self.server)
			with closing(HTTPConnection(host,port)) as con:
				con.request('GET', filepath)
				response = con.getresponse()
				self.modified = response.getheader('Last-Modified')
				status = response.status

				if status not in (200,204):
					print('Error occured',status)
			
				if status !=  204:
					self.write(response.read())

				if 'r' in mode:
					self.seek(0)

				self.lockid = ''

		if 'a' in mode or 'w' in mode:
			host,port = utils.get_port(_config['lockserver'])
			self.lockid = int(utils.Locked(path, host, port))

		if 'c' in mode:
			File._cache[path] = self

	def __exit__(self, exc, value, tb):
		## Intimate changes to DFS, and close file

		self.close()

		if 'c' not in self.mode:
			return SpooledTemporaryFile.__exit__(self, exc, value, tb)

		return False

	
	def close(self):
		
		pass

	def flush(self):
		
		pass

	def commit(self):

		pass

	def from_cache(path):

		pass
def unlink(path):

	pass


def rename(path, newPath):

	with open(path) as f:
		with open(newPath, 'w') as newf:
			newf.write(f.read())
		
		## Unlink previous file from server

open = File

_config = { 'nameserver' : None,
	    'lockserver' : None,
	    'max_size' : 1024 ** 2
	  } 

File._cache = {}

utils.load_config(_config, 'client.dfs.json')
