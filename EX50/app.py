import web

urls = (
  '/', 'Index'
)

app = web.applications(urls, globals())

render = web.template.render('templates/')

class Index(objects):
    def GET(self):
        greetings = "Hello World"
        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()
