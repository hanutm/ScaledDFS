import web
import Namingserver 

	
url = { '(/.*)','NamingServer.NameServer' }

app = web.application(url, globals())

if __name__ == 'main':
	app.run()

