from google.appengine.ext import ndb

class Poster(ndb.Model):
    user_name = ndb.StringProperty()
    email_address = ndb.StringProperty()
    post_content = ndb.StringProperty()
