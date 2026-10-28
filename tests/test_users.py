import allure
import pytest
from utils.util import RequestUtil

datas = RequestUtil.read_yaml(RequestUtil.BASE_DIR + '/datas/user.yaml')

@allure.feature("创建成功")
@pytest.mark.parametrize("datas",datas['user_success'])
def test_create_success_user(datas):
    # datas = datas.get("success_data",[])
    response = RequestUtil.send_requests('POST',RequestUtil.BASEURL \
                                         + 'api/users',datas)
    res = response.json()
    # a = datas["except_code"]
    assert response.status_code == datas['except_code']
    # assert res["id"] is not None
# ********************************************************
@allure.feature("获取成功")
def test_fetch_success_user() :
    response = RequestUtil.send_requests('GET', RequestUtil.BASEURL \
                                         + 'api/users/2')
    res = response.json()
    assert response.status_code == 200
    assert res["data"]["first_name"] == "Janet"
    assert res["data"]["id"] == 2

@allure.feature("create_user")
def test_create_delete_user() :
    data = {"name": "morpheus", "job": "zion resident"}
    response = RequestUtil.send_requests("POST", RequestUtil.BASEURL + 'api/users',data)
    res = response.json()
    assert response.status_code == 201
    assert res['name'] == data['name']
    response = RequestUtil.send_requests("DELETE",RequestUtil.BASEURL+'api/users'+'/'+res['id'])
    assert response.status_code == 204

@allure.feature("update_user")
def test_update_user():
    data = {"name": "morpheus", "job": "zion resident"}
    response = RequestUtil.send_requests("PUT",RequestUtil.BASEURL+'api/users/2',data)
    res = response.json()
    assert response.status_code == 200
    assert res['name'] == 'morpheus'
    assert res["job"] == 'zion resident'

@allure.feature("更新用户")
def test_update_user_patch():
    resp = RequestUtil.send_requests("PATCH", RequestUtil.BASEURL + "api/users/2",
                                     {"name": "Xinghe", "job": "QA"})
    assert resp.status_code == 200
    assert resp.json()["name"] == "Xinghe"      # 值对不对

@allure.feature("查询未知用户")
def test_get_unknown_user_404():
    resp = RequestUtil.send_requests("GET", RequestUtil.BASEURL + "api/users/999", None)
    assert resp.status_code == 404              # 门的反面