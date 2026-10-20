import allure
import pytest
from utils.util import RequestUtil
requestUtil = RequestUtil()

datas = requestUtil.read_yaml(requestUtil.BASE_DIR + '/datas/user.yaml')

@allure.feature("创建成功")
@pytest.mark.parametrize("datas",datas['user_success'])
def test_create_success_user(datas):
    # datas = datas.get("success_data",[])
    response = requestUtil.send_requests('POST',requestUtil.BASEURL \
                                         + 'api/users',datas)
    res = response.json()
    # a = datas["except_code"]
    assert response.status_code == datas['except_code']
    # assert res["id"] is not None
# ********************************************************
@allure.feature("获取成功")
def test_fetch_success_user() :
    response = requestUtil.send_requests('GET', requestUtil.BASEURL \
                                         + 'api/users/2')
    res = response.json()
    assert response.status_code == 200
    assert res["data"]["first_name"] == "Janet"
    assert res["data"]["id"] == 2

@allure.feature("create_user")
def test_create_delete_user() :
    data = {"name": "morpheus", "job": "zion resident"}
    response = requestUtil.send_requests("POST", requestUtil.BASEURL + 'api/users',data)
    res = response.json()
    assert response.status_code == 201
    assert res['name'] == data['name']
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