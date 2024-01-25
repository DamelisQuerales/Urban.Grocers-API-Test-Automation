import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


def get_new_user_token():
    response = post_new_user(data.user_body)
    json = response.json()
    return json['authToken']


def post_new_client_kit(kit_body):
    auth_token = get_new_user_token()
    headers = {"Content-Type": "application/json",
               "Authorization": f"Bearer {auth_token}"
               }
    # Realiza una solicitud POST para crear un nuevo kit de producto
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers)
