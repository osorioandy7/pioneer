import webapp2
import os
import jinja2

env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("static_folder/main.html")
        self.response.out.write(template.render(var1 = "hi"))

class ForumHandler(webapp2.RequestHandler):
    def get(self):
        template2 = env.get_template("static_folder/forum.html")

class MapHandler(webapp2.RequestHandler):
    def get(self):
        template3 = env.get_template("static_folder/mapspage.html")
        self.response.out.write(template3.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/forum', ForumHandler),
    ('/map', MapHandler)
], debug=True)
