import json, os

from squarespace_orders_api import Squarespace

store = Squarespace(os.environ.get('SS_API_KEY'))

data = store.request_orders()
for order in data['result']:
	print(order['orderNumber'] + ': ' + order['billingAddress']['firstName'] + order['billingAddress']['lastName'])
	print(order['fulfillmentStatus'] + '\n')