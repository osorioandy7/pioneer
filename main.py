import webapp2
import os
import jinja2
from forum_database import Poster
import logging

env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("static_folder/main.html")
        self.response.out.write(template.render(var1 = "hi"))

class ForumHandler(webapp2.RequestHandler):
    def get(self):
        template2a = template2 = env.get_template("static_folder/forum.html")
        self.response.out.write(template2a.render())

class ForumNewQuestionHandler(webapp2.RequestHandler):
    def get(self):
        template2b = env.get_template("static_folder/forum_new_question.html")
        thomas = Poster(user_name = "Thomas", email_address = "thomas@usa.gov", post_content = "yayayayayyayy")
        key_thomas = thomas.put()
        thomas_name = key_thomas.get().user_name
        self.response.out.write(template2b.render(name = thomas_name))
    # def post(self):
    #     template2a = env.get_template("static_folder/mapspage.html")
    #     self.response.out.write(template2a.render())
    #     self.response.write("You have successfully submitted your post!" )

class MapHandler(webapp2.RequestHandler):
    def get(self):
        template3 = env.get_template("static_folder/mapspage.html")
        self.response.out.write(template3.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/forum', ForumHandler),
    ('/newforumpost', ForumNewQuestionHandler),
    ('/map', MapHandler)

], debug=True)
