import logging
import unittest

import requests

import utils
from api.ApiOrder import ApiOrder
from api.ApiLogin import ApiLogin
import app
from parameterized import parameterized


class TestOrder(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.session = requests.session()
        cls.obj_login = ApiLogin()
        cls.obj_order = ApiOrder()
        login_response = cls.obj_login.post_login(cls.session, {"username": "debug", "password": "debug123qwe",
                                                                "grant_type": "password"})
        access_token = login_response.json()['access_token']
        app.headers['Authorization'] = 'Bearer ' + access_token

    @classmethod
    def tearDownClass(cls) -> None:
        cls.session.close()

    @parameterized.expand(utils.get_json_param('data_order.json', 'test_order_search'))
    def test_order_search(self, title, param, response_assert):
        logging.info("title:{},param:{}".format(title, param))
        search_response = self.obj_order.get_order_search(self.session, param)
        logging.info("response:{}".format(search_response.json()))
        utils.assert_api_response(response_assert, search_response)
