from api.ApiLogin import ApiLogin
import unittest
import requests
import utils
from parameterized import parameterized
import logging


class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
        self.obj_login = ApiLogin()

    def tearDown(self) -> None:
        self.session.close()

    @parameterized.expand(utils.get_json_param('data_Login.json', 'test_login'))
    def test_login(self, title, param, dic_assert):
        logging.info('titlt:{},param:{}'.format(title, param))
        response = self.obj_login.post_login(self.session, param)
        logging.info('response:{}'.format(response.json()))
        utils.assert_api_response(dic_assert, response)
