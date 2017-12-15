import web

import LockServer

url = ( '(/.*)','LockServer.LockServer')

app = web.application(url, globals())

if __name__ == '__main__':
	app.run()
