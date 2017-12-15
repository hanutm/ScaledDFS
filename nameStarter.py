import web
import nameserver

	
url = { '(/.*)','nameserver.Nameserver' }

app = web.application(url, globals())

if __name__ == 'main':
	app.run()

