import web

import Server.py

url = ( '(/.*)', 'Server.fileServer')

app.webapplication(url, globals())


if __name__ == '__main__':
	app.run()

