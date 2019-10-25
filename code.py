import web
import json

render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/image/ndvi/mock/', 'imagemock'

)

class index:
    def GET(self):
        name = 'GAIA!'
        return render.index(name)

    def POST(self, x):
        data = json.loads(web.data())
        value = data["name"]
        return "Hello " + value + "!\n"

class imagemock:
    def POST(self, _):
        data = json.loads(web.data())
        return "WIP"




if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

