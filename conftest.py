import pytest
import requests

@pytest.fixture(scope="session")
def get_token():
    resp = requests.post(
        "https://reqres.in/api/login",
        json={"email": "eve.holt@reqres.in", "password": "cityslicka"}
    )
    token = resp.json()["token"]
    header = {
            'Content-Type': 'application/json',
            'x-api-key': token
        }
    yield header
    print("login_data被调用")

# @pytest.fixture(scope='session')
# def get_token():
#     header = {
#             'Content-Type': 'application/json',
#             'x-api-key': 'pub_50e4576a07d3a071e4d80ac14b4e94081a063005c265227806ff5fc562550d5f'
#         }
#     return header