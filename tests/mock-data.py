import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

from webhook.app.src.schemas import AccountBody, CardBody, PersonBody

person_data = PersonBody(
    id=2,
    name="João da Silva",
    email="paulo.guedes@example.com",
    gender="M",
    birth_date="1990-01-01",
    address="Rua Exemplo, 123",
    salary=5000.0,
    cpf="12345678901"
)

account_data = AccountBody(
    id=1,
    status_id=0,
    due_day=10,
    person_id=1,
    balance=10000,
    avaliable_balance=6000
)

card_data = CardBody(
    id=1,
    card_number="5500989867560184",
    account_id=1,
    status_id=0,
    limit=15000,
    expiration_date="09/29"
)

# Serializar para JSON


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

test_json = person_data.model_dump_json()

encrypted_body = encrypt_body(test_json, "./public_key.pem")
encrypted_body_base64 = base64.b64encode(encrypted_body).decode('utf-8')
print(encrypted_body_base64)

# person
# hApOWpAP519r1vrBfWMSO4k+qX28/d+hsqsIKpZcYkYezGvyPSFVnQ1H/5jWucndqXgovoCVrPZx6cMX2hBdF7UkySbXvoe50+1dy0HMwlLdNw5k0GqSnWKY/V7i1kt8CsVrcpHQ0PeOGWdSdkUFC8lBweh1cx3BwJ0s7dDdKtb0DCEx9mAcOeoKzG6DLMFJui3INFAp2/X55tHfqWhEC+GaVkVcBmtPAVWr651ESMTLZIN2Lcdbq82GpfWyvtAD6tmqkFUYEb9yVyLEQ2Vz0H8obS5Xw1igIZMXrNCV1FttcggOCIrSgRitSs53fWMk6Qb3tye7OjSIO1NKtutgQw==


# account
# ZecOar+43Au1Ac5aqiDLObLh7JqrctJ2M91Rger7acTBJowcykG7hYCdN/ole47pNKSjIEbTny2RUU97QHBTEvjGVhrSNN6QNGHBfZr8uFh/mu6HG5D2wQA59CJ9RvUlx8PzlHCnHoKDr0E44TpWPr1HqgLXu6uN15hN79bjQ7SgNj3kkVwdGipJjJK/u27pefHVkBNCsjR/MvESfTDOKMQrZpIqeRbclKWoL5QJL+Yuqed2IVZ/k4ILooebyAZdK5RIbWA7Onzkez4zSmJGaFqAQ3OCKgZSCoVtxgmYIgBBtwHbSDXQM2V9LhKF1Sz8YSl3VQJo4JA0QXlGJ64UHA==

# card
# EgGJz4BCiFX+4JNhqCV5EfJqigB4dXcfjY6eIpr5ZC0duE19AtD9D/y2d7IS/teOJCmwMUCB5LuypZ2CdINgrOOdGTggHXwgUxMpOc2UGKHux/rb7DJjoVV3aPy/bXC10IOzRrU6+6rmCy9G7HORSkKtX59fzEMt20pNdp+BZmHDZGZVvXWA6aC5PlRtlKQXYqI27WB/+z2LteGXUmxMuwC2ZgPb/tlP6DYSGbJw/BAe8Le/d3qsQzZSTGaycFMmrv1Kj80BbQ9K77XUoSCRu6u/uoV+pI9aMXYTq/a1RlzcON9DrT7CzJMMAkbaWensLRdNaCbMXGBt70JIfJhdmA==