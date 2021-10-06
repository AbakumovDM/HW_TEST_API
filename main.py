import requests
import unittest

token = TOKEN

class TestYandexApi(unittest.TestCase):
    def test_yadisk_api(self):
        url = "https://cloud-api.yandex.net:443/v1/disk/resources"
        headers = {'Authorization': f'OAuth {token}'}
        params = {"path": 'HW_TEST'}
        response = requests.put(url=url, headers=headers, params=params)
        actual_res = response.status_code
        expected_res = 201
        self.assertEqual(expected_res, actual_res)

    def test_yadisk_folder_already_exists(self):
        url = "https://cloud-api.yandex.net:443/v1/disk/resources"
        headers = {'Authorization': f'OAuth {token}'}
        params = {"path": 'HW_TEST2'}
        response = requests.put(url=url, headers=headers, params=params)
        actual_res = response.status_code
        expected_res = 409
        self.assertEqual(expected_res, actual_res)

    def test_yadisk_not_authorized(self):
        url = "https://cloud-api.yandex.net:443/v1/disk/resources"
        headers = {'Authorization': 'OAuth '}
        params = {"path": 'HW_TEST2'}
        response = requests.put(url=url, headers=headers, params=params)
        actual_res = response.status_code
        expected_res = 401
        self.assertEqual(expected_res, actual_res)