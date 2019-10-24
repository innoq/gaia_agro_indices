import web
import json

render = web.template.render('templates/')

urls = (
    '/(.*)', 'index'
)

class index:
    def GET(self, name):
        return render.index(name)

    def POST(self, x):
        print ("x is", x)
        data = json.loads(web.data())
        value = data["name"]
        return "Hello " + value + "!"


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

