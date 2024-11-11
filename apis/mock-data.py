import base64
import os

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from faker import Faker
from webhook.app.src.schemas import AccountBody, CardBody, PersonBody


class IDGenerator:
    def __init__(self, start=1):
        self.current_id = start

    def get_next_id(self):
        next_id = self.current_id
        self.current_id += 1
        return next_id


fake = Faker('pt_BR')
person_id = IDGenerator(start=1)
account_id = IDGenerator(start=1)
card_id = IDGenerator(start=1)
address = f"{fake.street_name()}, {fake.building_number()}, {fake.city()}, {fake.state_abbr()}"
balance = round(fake.random.uniform(1000, 30000), 2)
avaliable_balance = round(fake.random.uniform(0, balance), 2)

person_data = PersonBody(
    id=person_id.get_next_id(),
    name=fake.name(),
    email=fake.email(),
    gender=fake.random_element(elements=('M', 'F')),
    birth_date=fake.date_of_birth(minimum_age=18, maximum_age=90).isoformat(),
    address=address,
    salary=round(fake.random.uniform(2000, 20000), 2),
    cpf=fake.cpf().replace('.', '').replace('-', '')
)

account_data = AccountBody(
    id=account_id.get_next_id(),
    status_id=fake.random_int(min=0, max=3),
    due_day=fake.random_int(min=1, max=30),
    person_id=person_data.id,
    balance=balance,
    avaliable_balance=round(fake.random_number(digits=4), 2)
)

card_data = CardBody(
    id=card_id.get_next_id(),
    card_number=fake.credit_card_number(),
    account_id=account_data.id,
    status_id=fake.random_int(min=0, max=3),
    limit=round(fake.random_number(digits=5), 2),
    expiration_date=fake.credit_card_expire()
)


def load_public_key(public_key_path):
    """
    Carrega a chave pública de um caminho fornecido, verificando se o arquivo existe.
    """
    if os.path.exists(public_key_path):
        with open(public_key_path, "rb") as key_file:
            public_key = serialization.load_pem_public_key(key_file.read())
        return public_key
    else:
        raise FileNotFoundError(f"O arquivo de chave pública não foi encontrado em: {public_key_path}")


def split_data(data, chunk_size):
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]


def encrypt_body(body, public_key_path, chunk_size=190):
    public_key = load_public_key(public_key_path)
    chunks = split_data(body.encode('utf-8'), chunk_size)

    encrypted_chunks = []
    for chunk in chunks:
        encrypted_chunk = public_key.encrypt(
            chunk,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        encrypted_chunks.append(encrypted_chunk)

    encrypted_body = b''.join(encrypted_chunks)
    return encrypted_body


person = person_data.model_dump_json()
account = account_data.model_dump_json()
card = card_data.model_dump_json()


def encrypt(json, json_name):
    public_key_path = os.path.join(os.path.dirname(__file__), "../secrets/public_key.pem")

    encrypted_body = encrypt_body(json, public_key_path)
    encrypted_body_base64 = base64.b64encode(encrypted_body).decode('utf-8')

    print(f"Body de {json_name}:\n")
    print(encrypted_body_base64, end="\n\n")


encrypt(person, "person")
encrypt(account, "account")
encrypt(card, "card")
