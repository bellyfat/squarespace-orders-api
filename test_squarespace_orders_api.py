import json, os, unittest

from squarespace_orders_api import Squarespace

store = Squarespace(os.environ.get('SS_API_KEY'))

class TestSquarespace(unittest.TestCase):
	"""
	Tests actual order data against the order data received through the 
	squarespace_orders_api module.
	"""

	def test_request_order(self):
		""" 
		Performs a live request to Squarespace for a given 
		order and compares its json data to the data in `test_order.json`.
		"""
		global store
		order_id = 'your_order_id'
		order_data = store.request_order(order_id=order_id)
		with open('test_order.json') as json_file:
			actual_order_data = json.load(json_file)
			self.assertTrue(actual_order_data == order_data, msg='Individual orders are not identical.')

	def test_request_orders(self):
		""" 
		Performs a live request to Squarespace for the first 50
		orders and compares its json data to the data in `test_orders.json`.
		"""
		global store
		order_data = store.request_orders()
		with open('test_orders.json') as json_file:
			actual_order_data = json.load(json_file)
			self.assertTrue(actual_order_data['result'] == order_data['result'], msg='Orders are not identical.')