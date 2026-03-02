import allure
import json
from utils.util import RequestUtil
requestUtil = RequestUtil()

@allure.feature("fetch_user")
def test_fetch_user() :
    response = requestUtil.send_requests("GET", requestUtil.BASEURL+'api/users/2')
    res = response.json()
    assert response.status_code == 200
    assert res["data"]["first_name"] == "Janet"
    assert res["data"]["id"] == 2

@allure.feature("create_user")
def test_create_delete_user() :
    file = open(requestUtil.BASE_DIR + '/data/user.json',"r")
    inputData = json.loads(file.read())
    response = requestUtil.send_requests("POST",requestUtil.BASEURL+'api/users',inputData)
    res = response.json()
    assert response.status_code == 201
    assert res['name'] == inputData['name']
    response = requestUtil.send_requests("DELETE",requestUtil.BASEURL+'api/users'+'/'+res['id'])
    assert response.status_code == 204

@allure.feature("update_user")
def test_update_user():
    data = {"name": "morpheus", "job": "zion resident"}
    response = requestUtil.send_requests("PUT",requestUtil.BASEURL+'api/users/2',data)
    res = response.json()
    assert response.status_code == 200
    assert res['name'] == 'morpheus'
    assert res["job"] == 'zion resident'