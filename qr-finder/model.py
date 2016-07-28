from google.appengine.ext import ndb

class ItemModel(ndb.Model):
	#euuid = ndb.StringProperty(required=True)
	name = ndb.StringProperty(required=True)
	description = ndb.StringProperty(default="No description")
	price = ndb.FloatProperty(required=True, default=0)

class LogModel(ndb.Model):
	#euuid = ndb.StringProperty(required=True)
	item = ndb.KeyProperty(kind=ItemModel)
	newprice = ndb.FloatProperty(required=True, default=0)
	discount = ndb.IntegerProperty(required=True, default=0)
	amount = ndb.IntegerProperty(required=True, default=1)
	selldate = ndb.DateProperty(auto_now_add=True)
		