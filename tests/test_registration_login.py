import allure
import json
from utils.util import RequestUtil
requestUtil = RequestUtil()

@allure.feature("注册成功")
def test_successful_registration() :    # 注册成功
    all_params = requestUtil.read_yaml(requestUtil.BASE_DIR + "/data/registration.yaml")
    params = all_params.get('registration_success',[])
    for param in params :
        data = {
            'email': param['email'],
            'password': param['password']
        }
        response = requestUtil.send_requests("POST",requestUtil.BASEURL+'api/register',data)
        # response = safe_post(url, header, data)
        responseJson = json.loads(response.text) # 将json字符串解析为python对象responseJson
        assert response.status_code == 200
        assert "token" in responseJson
        assert responseJson["token"] is not None
        assert "error" not in responseJson

@allure.feature("注册失败")
def test_unsuccessful_registration() :
    all_params = requestUtil.read_yaml(requestUtil.BASE_DIR + "/data/registration.yaml")
    params = all_params.get('registration_fail', [])
    data = {
        'email': params['email'],
        'password': params['password']
    }
    response = requestUtil.send_requests("POST",requestUtil.BASEURL+'api/register',data)
    responseJson = json.loads(response.text)
    assert response.status_code == params['expect_code']
    assert "error" in responseJson
    assert responseJson['error'] is not None
    assert "token" not in responseJson

@allure.feature("登录成功")
def test_successful_login():
    all_params = requestUtil.read_yaml(requestUtil.BASE_DIR + "/data/login.yaml")
    params = all_params.get('login_success', [])
    for param in params :
        data = {
            'email': param['email'],
            'password': param['password']
        }
        response = requestUtil.send_requests("POST",requestUtil.BASEURL+'api/login',data)
        responseJson = json.loads(response.text)
        assert response.status_code == 200
        assert "token" in responseJson
        assert responseJson["token"] is not None
        assert "error" not in responseJson

@allure.feature("登录失败")
def test_unsuccessful_login() :
    all_params = requestUtil.read_yaml(requestUtil.BASE_DIR + "/data/login.yaml")
    params = all_params.get('login_fail', [])
    for param in params :
        data = {
            'email': param['email'],
            'password': param['password']
        }
        response = requestUtil.send_requests("POST",requestUtil.BASEURL+'api/register',data)
        responseJson = json.loads(response.text)
        assert response.status_code == param['expect_code']
        assert "error" in responseJson
        assert responseJson['error'] is not None
        assert "token" not in responseJson





