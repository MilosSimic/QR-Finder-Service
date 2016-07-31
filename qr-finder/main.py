import endpoints
from protorpc import remote
from messages import InsertItem, SellItem, Return, DeleteItem
from messages import ItemLog, ItemLogCollection, ReportItem
from model import ItemModel, LogModel
from protorpc import message_types

@endpoints.api(name='item_reader', version='v1')
class ItemReaderAPI(remote.Service):

	@endpoints.method(InsertItem, Return, 
		path='item_insert', http_method='POST', name='item_reader.insert')
	def item_insert(self, request):
		item = ItemModel.get_by_id(request.uuid)

		if item:
			ItemModel(price = request.price, name = request.name, description = request.description).put()
			return ReturnMessage(message="Item updated")
		
		ItemModel(id = request.uuid, price = request.price, name = request.name, description = request.description).put()
		return Return(message="Item inserted")

	@endpoints.method(SellItem, Return, 
		path='item_sell', http_method='POST', name='item_reader.sell')
	def item_sell(self, request):
		item = ItemModel.get_by_id(request.uuid)

		if item:
			log = LogModel()
			log.item = item.key
			log.discount = request.discount
			log.amount = request.amount

			if request.discount > 0:
				old_price = item.key.get().price - (item.key.get().price * (float(request.discount) / 100.0))
				log.newprice = old_price
			else:
				log.newprice = item.key.get().price

			log.put()

			print item.key.get().name.encode('utf-8').strip(), log.newprice

			return Return(message="{} sold, total price: {}".format(item.key.get().name.encode('utf-8').strip(), log.newprice))

		return Return(message="Item not exists")

	@endpoints.method(SellItem, Return, 
		path='item_remove', http_method='DELETE', name='item_reader.delete')
	def item_remove(self, request):
		item = ItemModel.get_by_id(request.uuid)

		if item:
			item.key.delete()
			return Return(message="Item deleted")

		return Return(message="Item not exists")

	@endpoints.method(message_types.VoidMessage, ItemLogCollection, 
		path='items_log', http_method='GET', name='item_reader.log')
	def items_log(self, request):
		my_items = []

		for record in LogModel.query():
			item = record.item.get()

			log = ItemLog(price = item.price, name = item.name, newprice = record.newprice, discount = record.discount, 
				amount = record.amount, selldate = str(record.selldate))
			my_items.append(log)

		return ItemLogCollection(items = my_items)

	@endpoints.method(ReportItem, ItemLogCollection, 
		path='items_report', http_method='GET', name='item_reader.report')
	def items_log_report(self, request):
		my_items = []

		for record in LogModel.query():
			if record.selldate.month == request.month:
				item = record.item.get()
				item_log = InsertItem(uuid = item.key.id(), price = item.price, name = item.name, description = item.description)

				log = ItemLog(item = item_log, newprice = record.newprice, discount = record.discount, amount = record.amount, 
					selldate = str(record.selldate))
				my_items.append(log)

		return ItemLogCollection(items = my_items)


api = endpoints.api_server([ItemReaderAPI])