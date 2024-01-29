headers = {
    "Content-Type": "application/json",
}

user_body = {
    "firstName": "Leonidas",
    "phone": "+11234567890",
    "address": "300 guerreros, Esparta"
}

# Cuerpos de las solicitudes incluidas en los test


class Kitname:
    kit_body_1 = {"name": "a"}
    kit_body_2 = {"name": "Abcdabcdabcdabcdabcdabc(se omitió para la brevedad)"}
    kit_body_3 = {"name": ""}
    kit_body_4 = {"name": "Abcdabcdabcdabcdabcdabcd(se omitió para la brevedad)"}
    kit_body_5 = {"name": "№%@"}
    kit_body_6 = {"name": " A Aaa "}
    kit_body_7 = {"name": "123"}
    kit_body_8 = {}
    kit_body_9 = {"name": 123}
