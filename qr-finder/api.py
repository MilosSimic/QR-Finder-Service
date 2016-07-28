import endpoints
from protorpc import remote
from messages import InsertItemMessage, SellItemMessage, ReturnMessage
from model import ItemModel
from protorpc import message_types

@endpoints.api(name='item_reader', version='v1')
class ItemReaderAPI(remote.Service):

	@endpoints.method(InsertItemMessage, ReturnMessage, 
		path='item_insert', http_method='POST', name='item_reader.insert')
	def item_insert(self, request):
		pass

	@endpoints.method(SellItemMessage, ReturnMessage, 
		path='item_sell', http_method='POST', name='item_reader.sell')
	def item_sell(self, request):
		pass