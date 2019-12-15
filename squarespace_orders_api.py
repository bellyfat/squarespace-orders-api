import requests, json

app_version = '1.0'
api_base_url = 'https://api.squarespace.com'
api_version = '1.0'
user_agent = 'Python Squarespace Orders API v' + api_version

class Squarespace(object):
    """
    The Squarespace class contains the various components needed to call the Squarespace Orders API.
    """

    def __init__(self, api_key, api_base_url=api_base_url, api_version=api_version):
        self.api_key = api_key
        self.api_base_url = api_base_url
        self.api_version = api_version

        self.http = requests.Session()
        self.http.headers.update({'Authorization': 'Bearer ' + self.api_key})
        self.http.headers.update({'User-Agent': user_agent + '/' + app_version})

    def request(self, path, args=None):
        """ Construct and send a request to Squarespace """
        url = '%s/%s/%s' % (self.api_base_url, self.api_version, path)
        return self.validate_request(self.http.get(url, params=args))

    def submit(self, path, object):
        """ Construct an endpoint to post data to Squarespace """
        url = '%s/%s/%s' % (self.api_base_url, self.api_version, path)
        return self.validate_request(self.http.post(url, json=object))

    def validate_request(self, request):
        """ Validates a request before sending """
        if request.status_code == 200 or request.status_code == 201:
            return request.json()
        elif 400 <= request.status_code <= 599:
            raise RuntimeError('Status code: ' + str(request.status_code))

    def request_order(self, order_id):
        """ 
        Requests a single order from the Squarespace Orders API: 
        https://developers.squarespace.com/commerce-apis/retrieving-an-order
        """
        uri = 'commerce/orders/' + order_id
        return self.request(uri)

    def request_orders(self, **args):
        """ 
        Requests a maximum of 50 orders from the Squarespace Orders API: 
        https://developers.squarespace.com/commerce-apis/retrieving-all-orders
        """
        uri = 'commerce/orders'
        return self.request(uri, args)

    def fulfill_order(self, **args):
        """ 
        Fulfills a given order: 
        https://developers.squarespace.com/commerce-apis/fulfilling-an-order
        """
        order_id = args['order_id']
        service = args['service']
        tracking_number = args['tracking_number']
        carrier = args['carrier_name']
        notification = str(args['notification'])
        uri = 'commerce/orders/' + order_id + '/fulfillments'
        fulfillment = {
            'shouldSendNotification': notification,
            'shipments': [
                {
                    "shipDate": "2019-01-29T22:19:26.980Z",
                    "carrierName": carrier,
                    "service": service,
                    "trackingNumber": tracking_number
                }
            ]
        }
        return self.submit(uri, fulfillment)