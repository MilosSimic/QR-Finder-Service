from protorpc import messages

class DeleteItem(messages.Message):
	uuid = messages.StringField(1, required=True)

class ReportItem(messages.Message):
	month = messages.IntegerField(1, required=True)
		
		
class InsertItem(messages.Message):
	uuid = messages.StringField(1, required=True)
	price = messages.FloatField(2, required=True)
	name = messages.StringField(4, required=True)
	description = messages.StringField(5)

class SellItem(messages.Message):
	uuid = messages.StringField(1, required=True)
	discount = messages.IntegerField(3, required=True)
	amount = messages.IntegerField(4, required=True)

class Return(messages.Message):
	message = messages.StringField(1)

class ItemLog(messages.Message):
	item = messages.MessageField(InsertItem, 1)
	newprice = messages.FloatField(2)
	discount = messages.IntegerField(3)
	amount = messages.IntegerField(4)
	selldate = messages.StringField(5)

class ItemLogCollection(messages.Message):
    """Collection of Greetings."""
    items = messages.MessageField(ItemLog, 1, repeated=True)
		
		