import json

import app


def get_json_param(filename, key):
    param_list = []
    file_path = app.base_path + '/data/' + filename
    with open(file_path, encoding='utf-8') as f:
        json_data = json.load(f)
        for i in json_data.get(key):
            param_list.append(tuple(i.values()))
    return param_list


def assert_api_response(dic_assert, response):
    json_response = response.json()
    for key, value in dic_assert.items():
        if key == 'response_code':
            assert value == response.status_code
        else:
            assert value == json_response[key]
