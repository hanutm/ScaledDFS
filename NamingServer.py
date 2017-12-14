### File naming service or a Directory Service which indexes file systems from all file servers
### Since more than one server can keep file systems, this file creates a class which can be
### accessed by specifying different ports

''' To add/improve, 
	Add exception handling
	Update server on all methods
	load names from server
'''



import os
import web ## to operate on web based API (GET/POST methods)

import shelve

class NamingServer:

        def GET(self, path):
                ## Return server details holding the requried file
                ## Takes absolute path for file
                ## reads from a list of files/directories already on a server
                ## returns accordingly

                web.header('Content-Type', 'text/plain; charset=UTF-8')
                path = str(path)

                if path == '/':
                        return '/n'.join('%s=%s' % (directory, _folders[directory])
                                for directory in sorted(_folders))

                directory = str(os.path.dirname(path))

                if directory in _folders:
                        return _folders[directory]

                ## if nothing found, notify client that file does not exist


        def POST(self, directory):

                pass

        def DELETE(self, directory):

                pass



def update(directory,server, add):
	##updates the directory for files, and names.

	if directory[-1] = '/':
		directory = os.path.dirname(directory)	

	if add == True:
		print('Adding directory to server',directory,server)
		_folders[directory] = server
	elif directory in _folders:
		print('Removing directory from server',directory,server)	
		del _folders[directory]

	else:
		print('Directory not accessible (Might not be present)')


_config = { 'dbfile' : 'names.db' }
## load initial config from each server about the PORT, IP

_names = shelve.open(_config['dbfile'])
