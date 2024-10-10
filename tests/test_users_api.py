import pytest
from utils.api_client import clients
import uuid

@pytest.fixture(scope = 'module')
def api_client():
    return clients()

def test_getuser(api_client):
    response = api_client.get('users')
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_create_user(api_client):
    user_data = {
        "name" : "bishnu1",
        "username" : "qa user",
        "email" : "test@gmail.com"
    }
    response = api_client.post("users", user_data)
    print(response.json())
    assert response.status_code == 201
    assert response.json()["name"] == "bishnu1"
    id = response.json()['id']
    responseget = api_client.get("users/10")
    print(responseget.json())
    assert responseget.status_code == 200
    assert responseget.json()["name"] == "Clementina DuBuque"




# Every time we have to pass some different parameters value for name,email and username before creating user
# it is not possible , hence we add some codes in fixture and in test_Data.json and call the function here



def test_create_user(api_client, load_user_data):
    user_data = load_user_data["new_user"]
#every time we want to update the email with some new name. So we use uuid module
    unique_email = f"{uuid.uuid4().hex[:8]}@gmail.com"
    print(unique_email)
    user_data["email"] = unique_email
    response = api_client.post("users", user_data)
    print(response.json())
    assert response.status_code == 201
    assert response.json()["name"] == "bishnu"
    id = response.json()['id']
    responseget = api_client.get("users/11")
    print(responseget.json())






def test_update_user(api_client):
    user_data = {
            "name" : "bishnuR",
            "username" : "qa user",
            "email" : "test@gmail.com"
    }
    response = api_client.put("users/10", user_data)
    print(response.json())
    assert response.status_code == 200
    assert response.json()["name"] == "bishnuR"


def test_delete_user(api_client):
    response = api_client.delete("users/1")
    print(response.json())
    assert response.status_code == 200
    


