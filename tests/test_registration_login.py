import allure
import json
import pytest
from utils.util import RequestUtil

datas_frist = RequestUtil.read_yaml(RequestUtil.BASE_DIR + "/datas/registration.yaml")

@allure.feature("注册成功")
@pytest.mark.parametrize("datas_frist",datas_frist['registration_success'])
def test_successful_registration(datas_frist) :    # 注册成功
    # for param in params :
    #     data = {
    #         'email': param['email'],
    #         'password': param['password']
    #     }
    #     response = RequestUtil.send_requests("POST",RequestUtil.BASEURL+'api/register',data)
    #     # response = safe_post(url, header, datas)
    #     responseJson = json.loads(response.text) # 将json字符串解析为python对象responseJson
    #     assert response.status_code == 200
    #     assert "token" in responseJson
    #     assert responseJson["token"] is not None
    #     assert "error" not in responseJson
    response = RequestUtil.send_requests("POST",RequestUtil.BASEURL+'api/register',datas_frist)
    # response = safe_post(url, header, datas)
    responseJson = json.loads(response.text) # 将json字符串解析为python对象responseJson
    assert response.status_code == 200
    assert "token" in responseJson
    assert responseJson["token"] is not None
    assert "error" not in responseJson

@allure.feature("注册失败")
@pytest.mark.parametrize("datas_frist",datas_frist['registration_fail'])
def test_unsuccessful_registration(datas_frist) :
    response = RequestUtil.send_requests("POST",RequestUtil.BASEURL+'api/register',datas_frist)
    responseJson = json.loads(response.text)
    assert response.status_code != 200
    assert "error" in responseJson
    assert responseJson['error'] is not None
    assert "token" not in responseJson

datas_second = RequestUtil.read_yaml(RequestUtil.BASE_DIR + "/datas/login.yaml")

@allure.feature("登录成功")
@pytest.mark.parametrize("datas_second",datas_second['login_success'])
def test_successful_login(datas_second):
    response = RequestUtil.send_requests("POST",RequestUtil.BASEURL+'api/login',datas_second)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert "token" in responseJson
    assert responseJson["token"] is not None
    assert "error" not in responseJson

@allure.feature("登录失败")
@pytest.mark.parametrize("datas_second",datas_second['login_fail'])
def test_unsuccessful_login(datas_second) :
    response = RequestUtil.send_requests("POST",RequestUtil.BASEURL+'api/login',datas_second)
    responseJson = json.loads(response.text)
    assert response.status_code == datas_second['expect_code']
    assert "error" in responseJson
    assert responseJson['error'] is not None
    assert "token" not in responseJson





