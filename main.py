import webapp2
import os
import jinja2
from forum_database import Poster
import logging
from google.appengine.api import users
from google.appengine.ext import ndb
import urllib2

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

class ThreadsHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("static_folder/threads.html")
        self.response.out.write(template.render())
        user_search_term = self.request.get("search_term")

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
                <style>

                body{
                  background-color: #333333;
                }
                h1{
                  display: flex;
                  color: #bfff80;
                  font-family: 'Abel', sans-serif;
                  font-size: 45px;
                  justify-content: center;
                }

                h2{
                  display: flex;
                  color: white ;
                  font-family: 'Abel', sans-serif;
                  font-size: 30px;
                  justify-content: center;
                  text-align: center;
                }
                a{
                  display: flex;
                  justify-content: center;
                  font-size: 45;

                }



                </style>
                  <head>
                    <meta charset="utf-8">
                    <title>Sign up</title>


                  </head>
                  <body>
                    <h1> Forums </hr>
                      <h2> Sign up to join different discussion boards where you can ask questions, share stories, and give advice!
                       </h2>
                      <a href="%s">Sign in</a>
                  </body>''' % (
                    users.create_login_url('/forum')))

    def getForum(self):
        user = users.get_current_user()
        template2 = env.get_template("static_folder/forum.html")
        post_content = {}
        self.response.out.write(template2.render())

        template_variables = {
                        'user_name' : self.request.get('user_name'),
                        'email_address': user.email(),
                        'post_text': self.request.get('post_text'),
                        'thread_choice': self.request.get('thread_choice')
                            }
        user1 = Poster(user_name = template_variables['user_name'], email_address= template_variables['email_address'], post_text = template_variables['post_text'], thread_choice = template_variables['thread_choice']).put()


        user1_query = Poster.query()
        all_results = user1_query.fetch()



        signout_link_html = '<a href="%s">sign out</a>' % (
            users.create_logout_url('/forum'))
        self.response.out.write(signout_link_html)
        for result in all_results:
            #self.response.out.write(i)
            self.response.out.write("<div id='%s'><br>" % (template_variables['thread_choice']) + result.user_name + "<br>" + result.email_address + "<br>" + result.post_text + "</div>")
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
                        'post_text': self.request.get('post_text'),
                        'thread_choice': self.request.get('thread_choice')

                            }
        #user1 = Poster(user_name = template_variables['user_name'], email_address= template_variables['email_address'], post_text = template_variables['post_text']).put()


        user1_query = Poster.query()
        all_results = user1_query.fetch()

        signout_link_html = '<a href="%s">sign out</a>' % (
            users.create_logout_url('/forum'))
        self.response.out.write(signout_link_html)



        logging.info('Hello, doing some logging!')

        #uci_query = Poster.thread_choice
        #uci_results = uci_query.fetch()
        #
        #ucsd_query = Poster.query("thread_choice" "ucsd")
        #ucsd_results = ucsd_query.fetch()



        for result in all_results:
            #self.response.out.write(i)
            self.response.out.write("<div class='%s'><br>" % (result.thread_choice) + result.user_name + "<br>" + result.email_address + "<br>" + result.post_text + "</div>")
            logging.info(type(template_variables['thread_choice']))
            logging.info(template_variables['thread_choice'] + "\tplease")

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
    ('/threads',ThreadsHandler),
    ('/forum', ForumHandler),
    # ('/newforumpost', ForumNewQuestionHandler),
    ('/map', MapHandler),
    ('/about', AboutUsHandler),
    ('/college', CollegeHandler)

], debug=True)
