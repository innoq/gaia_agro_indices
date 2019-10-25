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
    def GET(self):
        web.header('Content-Type', 'image/png')
        with open('somefile.txt', 'a') as the_file:
            imageBinary = open("data/Hobbes.jpg", 'rb').read()
            #imageBinary = open("README.md", 'rb').read()
            return imageBinary
        return "Error 500"


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

