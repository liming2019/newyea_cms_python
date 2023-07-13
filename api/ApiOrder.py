import app


class ApiOrder:
    def __init__(self):
        self.url_order = app.host + '/api/newyea/order/page'

    def get_order_search(self, session, param):
        param_url = '&'.join([f'{key}={value}' for key, value in param.items()])
        return session.get(url=self.url_order + '?' + param_url, headers=app.headers)
