import allure
import json
import pytest
from utils.util import RequestUtil
from jsonschema import validate

datas_frist = RequestUtil.read_yaml(RequestUtil.BASE_DIR + "/datas/registration.yaml")

@allure.feature("注册成功")
@pytest.mark.parametrize("datas_frist",datas_frist['registration_success'])
def test_successful_registration(datas_frist) :    # 注册成功
    response = RequestUtil.send_requests("POST",RequestUtil.BASEURL+'api/register',datas_frist)
    # response = safe_post(url, header, datas)
    responseJson = json.loads(response.text) # 将json字符串解析为python对象responseJson
    # 注册成功响应的结构约定
    registration_success_schema = {
        "type": "object",
        "properties": {
            "token": {"type": "string", "minLength": 1}
        },
        "required": ["token"]          # token 必须存在，且必须是非空字符串
    }
    # 检查接口返回的数据是否符合约定的结构（校验函数）
    validate(instance=responseJson, schema=registration_success_schema)
    assert response.status_code == 200
    assert "token" in responseJson
    assert responseJson["token"] is not None
    assert "error" not in responseJson

@allure.feature("注册失败")
@pytest.mark.parametrize("datas_frist",datas_frist['registration_fail'])
def test_unsuccessful_registration(datas_frist) :
    response = RequestUtil.send_requests("POST",RequestUtil.BASEURL+'api/register',datas_frist)
    responseJson = json.loads(response.text)
    registration_fail_schema = {
        "type": "object",
        "properties": {
            "error": {"type": "string", "minLength": 1}
        },
        "required": ["error"]          
    }
    validate(instance=responseJson, schema=registration_fail_schema)
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
    login_success_schema = {
            "type": "object",
            "properties": {
                "token": {"type": "string", "minLength": 1}
            },
            "required": ["token"]          
        }
    validate(instance=responseJson, schema=login_success_schema)
    assert response.status_code == 200
    assert "token" in responseJson
    assert responseJson["token"] is not None
    assert "error" not in responseJson

@allure.feature("登录失败")
@pytest.mark.parametrize("datas_second",datas_second['login_fail'])
def test_unsuccessful_login(datas_second) :
    response = RequestUtil.send_requests("POST",RequestUtil.BASEURL+'api/login',datas_second)
    responseJson = json.loads(response.text)
    login_fail_schema = {
            "type": "object",
            "properties": {
                "error": {"type": "string", "minLength": 1}
            },
            "required": ["error"]          
        }
    validate(instance=responseJson, schema=login_fail_schema)
    assert response.status_code == datas_second['expect_code']
    assert "error" in responseJson
    assert responseJson['error'] is not None
    assert "token" not in responseJson





