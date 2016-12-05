import web

urls = (
  '/hello', 'Index'
)


app = web.applications(urls, globals())

render = web.template.render('templates/')

class Index(objects):
    def GET(self):
        form = web.input(name="Nobody")
        greeting = "Hello, %s" % form.name

        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()
