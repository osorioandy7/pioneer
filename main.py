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
        template2a = env.get_template("static_folder/forum.html")
        post_content = {}
        self.response.out.write(template2a.render())

    def post(self):
        result_template = env.get_template("static_folder/forum.html")
        template_variables = {'user_name' : self.request.get('user_name'),
                              'email_address': self.request.get('email_address'),
                              'post_content': self.request.get('post_content')
                            }
        Poster(user_name = template_variables['user_name'], email_address= template_variables['email_address']).put()

    #thePosters = Poster(user_name = template_variables['user_name'],  )

        thePosts = Posts(post_content = "fdoisjfiojfdissjdkkshdfjlodsf")
        self.response.out.write(template2a.render(post_content))
#user_name = ndb.StringProperty()
#email_address = ndb.StringProperty()
#post_content = ndb.StringProperty()
# class ForumNewQuestionHandler(webapp2.RequestHandler):
#     def get(self):
#         template2b = env.get_template("static_folder/forum_new_question.html")
#         thomas = Poster(user_name = "Thomas", email_address = "thomas@usa.gov", post_content = "yayayayayyayy")
#         key_thomas = thomas.put()
#         thomas_name = key_thomas.get().user_name
#         self.response.out.write(template2b.render(name = thomas_name))
    # def post(self):
    #     template2a = env.get_template("static_folder/mapspage.html")
    #     self.response.out.write(template2a.render())
    #     self.response.write("You have successfully submitted your post!" )

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
