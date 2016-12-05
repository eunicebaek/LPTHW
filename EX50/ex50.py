import web

urls = (
  '/', 'index'
)

app = web.applications(urls, globals())

class index:
    def GET(self):
        greeting = "Hello World"
        return greeting

if __name__ == "__main__":
    app.run()
  
