import webapp2
import os
import jinja2
from forum_database import Poster
import logging
from google.appengine.api import users
from google.appengine.ext import ndb


env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class CssiUser(ndb.Model):
    """CssiUser stores information about a logged-in user.

    The AppEngine users api stores just a couple of pieces of
    info about logged-in users: a unique id and their email address.

    If you want to store more info (e.g. their real name, high score,
    preferences, etc, you need to create a Datastore model like this
    example).
    """
    user_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    email = ndb.StringProperty()


class MainHandler(webapp2.RequestHandler):
    def get(self):

        template = env.get_template("static_folder/main.html")
        self.response.out.write(template.render())


class ForumHandler(webapp2.RequestHandler):
    # to show the page and template

    def get(self):
        user = users.get_current_user()
        # If the user is logged in...

        if user:
            email_address = user.nickname()
            # We could also do a standard query, but ID is special and it
            # has a special method to retrieve entries using it.

            # If the user has previously been to our site, we greet them!
            cssi_user = CssiUser.get_by_id(user.user_id())
            signout_link_html = '<a href="%s">sign out</a>' % (
                users.create_logout_url('/forum'))
            # if CssiUser.query(CssiUser.email == user.email()).get() == False:
            #     cssi_user_object = CssiUser(email=user.email(),user_name=user.nickname()).put()

            logging.info("Viewpage1")
            self.viewPage()
            logging.info("Viewpage3")
            # If the user hasn't been to our site, we ask them to sign up
        # Otherwise, the user isn't logged in!
        else:
            self.response.write('''
                Please log in to use our site! <br>
                <a href="%s">Sign in</a>''' % (
                    users.create_login_url('/forum')))

    def getForum(self):
        user = users.get_current_user()
        template2 = env.get_template("static_folder/forum.html")
        post_content = {}
        self.response.out.write(template2.render())

        template_variables = {
                        'user_name' : self.request.get('user_name'),
                        'email_address': user.email(),
                        'post_text': self.request.get('post_text')
                            }
        user1 = Poster(user_name = template_variables['user_name'], email_address= template_variables['email_address'], post_text = template_variables['post_text']).put()


        user1_query = Poster.query()
        all_results = user1_query.fetch()

        signout_link_html = '<a href="%s">sign out</a>' % (
            users.create_logout_url('/forum'))
        self.response.out.write(signout_link_html)
        for result in all_results:
            #self.response.out.write(i)
            self.response.out.write("<br>" + result.user_name + "<br>" + result.email_address + "<br>" + result.post_text)
            logging.info('Hello, doing some lOOOOOOOO!')


    def post(self):
        self.getForum()
    def viewPage(self):
        user = users.get_current_user()
        template2 = env.get_template("static_folder/forum.html")
        post_content = {}
        self.response.out.write(template2.render())

        template_variables = {
                        'user_name' : self.request.get('user_name'),
                        'email_address': user.email(),
                        'post_text': self.request.get('post_text')
                            }
        #user1 = Poster(user_name = template_variables['user_name'], email_address= template_variables['email_address'], post_text = template_variables['post_text']).put()


        user1_query = Poster.query()
        all_results = user1_query.fetch()

        signout_link_html = '<a href="%s">sign out</a>' % (
            users.create_logout_url('/forum'))
        self.response.out.write(signout_link_html)


        logging.info('Hello, doing some logging!')

        for result in all_results:
            #self.response.out.write(i)
            self.response.out.write("<br>" + result.user_name + "<br>" + result.email_address + "<br>" + result.post_text)
            logging.info('Hello, doing some lOOOOOOOO!')

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
