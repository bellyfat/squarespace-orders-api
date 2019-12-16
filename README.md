# Squarespace Orders API

A Python module to access the [Squarespace Orders API](https://developers.squarespace.com/commerce-apis/orders-api-overview).

```
data = store.request_orders()
for order in data['result']:
	print(order['orderNumber'])
```

## Prerequisites

* A Squarespace website eligible for orders and [API key](https://support.squarespace.com/hc/en-us/articles/236297987-Squarespace-API-keys#toc-orders-api)

## Getting Started

### Installation

* Create a virtual environment: `python3 -m venv env`
* Activate the environment: `source env/bin/activate`
* Add your API key as an environment variable: `export SS_API_KEY=<YOUR_API_KEY>`
* Install dependencies: `pip3 install -r requirements.txt`
* Run the application: `python3 test_api.py`

### Using the module

* Add your API key as an environment variable: `export SS_API_KEY=<YOUR_API_KEY>`
* Import the module: `import squarespace_orders_api`
* Access the API: `store = Squarespace(os.environ.get('SS_API_KEY'))`
* Request a single order: `order_data = store.request_order(order_id=order_id)`
* Request latest 50 orders: `order_data = store.request_orders()`
* Access data: `print(order_data['orderNumber'])`

## Making requests

`store = Squarespace(os.environ.get('SS_API_KEY'))`

#### request_order()

* Requests a single order from the Squarespace store.
* Keyword argument `order_id`: the `orderId` from the Squarespace store.
* See [Squarespace documentation](https://developers.squarespace.com/commerce-apis/retrieving-an-order) for further details.

#### request_orders()

* Requests a maximum of 50 orders from the Squarespace store.
* Optional keyword argument `cursor`: A string token, returned from the `pagination.nextPageCursor` of a previous response. Identifies where the next page of results should begin. If this parameter is not present or empty, the first page of order data will be returned.
* Optional keyword argument `modifiedAfter`: Type: An ISO 8601 date and time string, e.g. `2016-04-10T12:00:00Z`. Time-boxes request to orders that were modified after this time.
* Optional keyword argument `modifiedBefore`: Type: An ISO 8601 date and time string, e.g. `2016-04-10T12:00:00Z`. Time-boxes request to orders that were modified before this time.
* Optional keyword argument `fulfillmentStatus`: An enumerated string value of `PENDING`, `FULFILLED`, or `CANCELED`. Used to filter orders according to their fulfillment status.
* See [Squarespace documentation](https://developers.squarespace.com/commerce-apis/retrieving-all-orders) for further details.

Note that requests must not include multiple keyword arguments, except in the case of `modifiedAfter` and `modifiedBefore`.

#### fulfill_order()

* Sends a fulfillment request to the Squarespace store.
* Keyword argument `order_id`: specifies the order to update.
* Keyword argument `shouldSendNotification`: Indicates whether the customer should receive an email notification about the added shipments.
* Keyword argument `shipDate`: The ISO 8601 date and time representing the moment the shipment occurred.
* Keyword argument `carrierName`: A string representing the parcel service transporting the shipment.
* Keyword argument `service`: A string representing the level of service, as offered by the carrier, used for this shipment.
* Keyword argument `trackingNumber`: A string representing the carrier-generated tracking number.
* Keyword argument `trackingUrl` (optional): A tracking URL, ideally supplied by the carrier. If this value is provided, it must represent a valid URL.
* See [Squarespace documentation](https://developers.squarespace.com/commerce-apis/fulfilling-an-order)  for further details.

## Tests

Running tests: `python3 -m unittest test_squarespace_orders_api.py`

* `test_request_order`: Performs a live request to Squarespace for a given order and compares its json data to the data in `test_order.json`.
* `test_request_orders`: Performs a live request to Squarespace for the first 50 orders and compares its json data to the data in `test_orders.json`.

#### test_request_order: 

* Ensure API key is added to environment variable `SS_API_KEY`
* Ensure the `order_id` is set to a live `orderId` for your Squarespace store
* Ensure the json data for that particular order is added to the `test_order.json` file

#### test_request_orders:

* Ensure API key is added to environment variable `SS_API_KEY`
* Ensure the json data for that particular order is added to the `test_orders.json` file
* The `pagination.nextPageCursor` is not constant, so ensure that the assertion is based off `actual_order_data['result']` as opposed to just `actual_order_data`, which omits the `pagination` object entirely and focuses on just the `result` (i.e. the orders).

**Tip:** the json data for that particular order can be gotten using cURL: `curl "https://api.squarespace.com/1.0/commerce/orders/<your_order_id>" -H "Authorization: Bearer <your_api_key>"`. For more information, see [Squarespace's documentation](https://developers.squarespace.com/commerce-apis/retrieving-an-order). Similarly, the json data for the first 50 orders can be gotten using `curl "https://api.squarespace.com/1.0/commerce/orders/" -H "Authorization: Bearer <your_api_key>"`.

## Contributing & Support

For support, bug reporting, feature requests, improvements, suggestions or questions, please feel free to submit a pull request or open an issue.

## License

Copyright 2019 @ w-red-1

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.