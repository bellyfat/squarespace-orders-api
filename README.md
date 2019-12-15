# Squarespace Orders API

A Python module to access the [Squarespace Orders API](https://developers.squarespace.com/commerce-apis/orders-api-overview).

```
data = store.request_orders()
for order in data['result']:
	print(order['orderNumber'])
```

## Prerequisites

* A Squarespace website eligible for orders and [API key](https://support.squarespace.com/hc/en-us/articles/236297987-Squarespace-API-keys#toc-orders-api)

## Accessing the API

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