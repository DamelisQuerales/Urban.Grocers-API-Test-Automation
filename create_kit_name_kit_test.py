import sender_stand_request
import data

# Comprueba que la creación de un kit con el nombre especificado tiene éxito


def positive_assert(kit_body):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = kit_body
    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    # Comprueba si el código de estado es 201
    assert kit_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert kit_response.json()["name"]

# Pruebas que comprueban que la creación de un kit con el nombre especificado tiene éxito.

# Prueba 1. El número permitido de caracteres (1)


def test_create_kit_1_letter_in_name_get_success_response():
    kit_body = data.Kitname.kit_body_1
    positive_assert(kit_body)

# Prueba 2. El número permitido de caracteres (511)


def test_create_kit_511_letter_in_name_get_success_response():
    kit_body = data.Kitname.kit_body_2
    positive_assert(kit_body)

# Prueba 3. Se permiten caracteres especiales


def test_create_kit_special_symbol_in_name_get_success_response():
    kit_body = data.Kitname.kit_body_5
    positive_assert(kit_body)

# Prueba 4. Se permiten espacios


def test_create_kit_has_space_in_name_get_error_response():
    kit_body = data.Kitname.kit_body_6
    positive_assert(kit_body)

# Prueba 5. Se permiten números


def test_create_kit_has_number_in_name_get_error_response():
    kit_body = data.Kitname.kit_body_7
    positive_assert(kit_body)

#  Comprueba que la creación de un kit con el nombre especificado genera un error 400


def negative_assert_code_400(kit_body):

    # Comprueba si la variable "response" almacena el resultado de la solicitud.
    response = sender_stand_request.post_new_client_kit(kit_body)

    # Comprueba si la respuesta contiene el código 400.
    assert response.status_code == 400

    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400.
    assert response.json()["code"] == 400


# Prueba 6. Error. El parámetro firstName contiene 1 carácter

def test_create_kit_no_symbol_in_kit_name_get_error_response():
    kit_body = data.Kitname.kit_body_3
    negative_assert_code_400(kit_body)

# Prueba 7. Error. El número de caracteres es mayor que la cantidad permitida (512):


def test_create_kit_512_letter_in_first_name_get_error_response():
    kit_body = data.Kitname.kit_body_4
    negative_assert_code_400(kit_body)


# Prueba 8. El parámetro no se pasa en la solicitud
def test_create_kit_has_number_in_name_error_response():
    kit_body = data.Kitname.kit_body_8
    negative_assert_code_400(kit_body)


# Prueba 9. Se ha pasado un tipo de parámetro diferente

def test_create_kit_different_parameter_no_kit_name():
    kit_body = data.Kitname.kit_body_9
    negative_assert_code_400(kit_body)
