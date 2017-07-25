from google.appengine.ext import ndb

class Poster(ndb.Model):
    user_name = ndb.StringProperty()
    email_address = ndb.StringProperty()

class Posts(ndb.Model):
    post_content = ndb.StringProperty()
