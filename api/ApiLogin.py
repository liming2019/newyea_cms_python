import app


class ApiLogin:
    def __init__(self):
        self.url_login = app.host + '/api/auth/oauth/token'

    def post_login(self, session, data):
        # url_param = ''.join([f'{key}={value}&' for key, value in data.items()])[:-1]
        url_param = '&'.join([f'{key}={value}' for key, value in data.items()])
        return session.post(url=self.url_login + '?' + url_param, headers=app.headers)
