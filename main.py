import webapp2
import os
import jinja2
from forum_database import Poster
import logging

env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("static_folder/main.html")
        self.response.out.write(template.render())

class ForumHandler(webapp2.RequestHandler):
    # to show the page and template
    def get(self):
        template2a = env.get_template("static_folder/forum.html")
        post_content = {}
        self.response.out.write(template2a.render())
    # to get responses from the user input boxes
    def post(self):
        result_template = env.get_template("static_folder/forum.html")
        template_variables = {'user_name' : self.request.get('user_name'),
                              'email_address': self.request.get('email_address'),
                            }
        user1 = Poster(user_name = template_variables['user_name'], email_address= template_variables['email_address'])

        user1.put()
        user1_query = Poster.query()
        all_results = user1_query.fetch()

    #thePosters = Poster(user_name = template_variables['user_name'],  )
    #thePosts = Posts(post_content = "fdoisjfiojfdissjdkkshdfjlodsf")
        self.response.out.write(result_template.render(post_content= all_results[0].email_address))

class MapHandler(webapp2.RequestHandler):
    def get(self):
        template3 = env.get_template("static_folder/mapspage.html")
        self.response.out.write(template3.render())

class AboutUsHandler(webapp2.RequestHandler):
    def get(self):
        template4 = env.get_template("static_folder/aboutUs.html")
        self.response.out.write(template4.render())

class CollegeHandler(webapp2.RequestHandler):
    def get(self):
        template5 = env.get_template("static_folder/College101.html")
        self.response.out.write(template5.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/forum', ForumHandler),
    # ('/newforumpost', ForumNewQuestionHandler),
    ('/map', MapHandler),
    ('/about', AboutUsHandler),
    ('/college', CollegeHandler)

], debug=True)
