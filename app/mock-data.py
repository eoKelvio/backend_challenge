import base64
import json
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

from src.schemas import AccountBody, CardBody, PersonBody

person_data = PersonBody(
    person_id=1,
    name="João da Silva",
    email="joao.silva@example.com",
    gender="M",
    birth_date="1990-01-01",
    address="Rua Exemplo, 123",
    salary=5000.0,
    cpf="12345678901"
)

account_data = AccountBody(
    account_id=1,
    status_id=0,
    due_day=10,
    person_id=1,
    balance=10000,
    avaliable_balance=6000
)

card_data = CardBody(
    card_id=1,
    card_number="5500989867560184",
    account_id=1,
    status_id=0,
    limit=15000,
    expiration_date="09/29"
)

# Serializar para JSON
person_json = person_data.model_dump_json()

# Carregar a chave pública
def load_public_key(public_key_path):
    with open(public_key_path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(key_file.read())
    return public_key

# Encriptar os dados
def encrypt_body(body, public_key_path):
    public_key = load_public_key(public_key_path)
    encrypted_body = public_key.encrypt(
        body.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_body

encrypted_body = encrypt_body(person_json, "./public_key.pem")
encrypted_body_base64 = base64.b64encode(encrypted_body).decode('utf-8')
print(encrypted_body_base64)

# person
# dvTBNbMgo9eAs5cXLXWntTq6jlK/IC9zGm1SFuptWmpqtKjJNiRRvWVW2TZf8AfYoNswhNkbefV3u0l3WEBKNyTqEb4GJP4lQ/w++WepXS3F0vuVOlgbUAjrJIpRSD2pvifeGdiNRoeRINLH2KjXejYATa/NUtW7M7Iajwfz3qpD1clHzfkTYdFlbK5hbuOqtlPuAaq0QOh74iCensUmMh3Uvw7fFr95v8MfBoZ3T1RR0aFQ+J3hXQk1LzAQEXfkLHT5MZyfR7ya7QP/YWtRy088vlNt/rStdNE0mMQO7zkeApMqUXx4REWkkTNXzR0FVVqSjQa3NO33tAOwDb8vGQ==


# account
# CrHsrpRt1h+UHIir0Piedu9+8pLgqLvo23CXnXAL32rL4QwbNRdkakIiWPSAgs5cDULexlfx7zxjC2eQCABeKxu56n/4K3NJSxCUtF4H+tQdulRF6K5D9TPt0BL2OtO3RUKyyiwrZPcxGQy6Df6Kp/e6taSdjVmY/zOE3Kqs6utDSt/kbb0u1iVCFJwto+3bDPKHRiR482WgMWsiPV1kL4yZ9nr0xwwOpDn0P5lsYrIeXnAyebLcTPdsnUGVFKCPDwD2yErN+6a4n/dgee+CbJPpWEksFMLDgx4AbOr8L1dG/9UueoXO77XjyfeAVLFpNVDqR3PpU0AFcGy15IdQwA==

# card
# vNaqBpDgBF9U4W6r+15Jei5wljNpHQ30Z6t21PauvpOO6ucQI5Dnc+0ocKM4mMKWzZDGoIhWyAWLvE9Tw5etZRVpu6OwTb4blCE7yWWnyr8NRLKjx2qudPw6pelJHstdAqqCFvTjpgDuueZr6ruZ+x1MtXYUwE+aN76fWqOf9AWl4TVs6XlqJ81TvDNGxIzHPjVAmy526eNPE1yHgHLlVfP5Vq6IauKBbTXICsuwLViPfcrBsc5ZdeC2fnQBmWKlaNf8EO8Eq/Un7eqeO2oEjYq97rFFRpq5prcM5XUkh8wh0JJjsWg9o8o+tWV1KRa4yNbaTVIPQyBumMFiR0InoQ==