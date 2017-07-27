from google.appengine.ext import ndb

class Poster(ndb.Model):
    user_name = ndb.StringProperty()
    email_address = ndb.StringProperty()
    post_text = ndb.StringProperty()
    thread_choice = ndb.StringProperty()
