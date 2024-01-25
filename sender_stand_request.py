import configuration
import requests
import data

# Esta función se utiliza para crear un nuevo usuario


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

# Esta función se utiliza para obtener un token de autenticación para un nuevo usuario


def get_new_user_token():
    # Captura la respuesta de la solicitud y la almacena en la variable response.
    response = post_new_user(data.user_body)
    json = response.json()
    # Extrae el campo authToken del objeto JSON y lo devuelve.
    return json['authToken']

# Esta función se utiliza para obtener crear un nuevo kit con el token de autenticación


def post_new_client_kit(kit_body):
    auth_token = get_new_user_token()
    # inserta los encabezados
    headers = {"Content-Type": "application/json",
               "Authorization": f"Bearer {auth_token}"
               }
    # Realiza una solicitud POST para crear un nuevo kit de producto
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         # Concatenación de URL base y ruta.
                         json=kit_body,
                         headers=headers)
