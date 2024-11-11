from cryptography.exceptions import UnsupportedAlgorithm
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding


def load_private_key(private_key_path, password=None):
    with open(private_key_path, "rb") as key_file:
        try:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=password.encode() if password else None,
            )
        except TypeError:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
            )
        except ValueError:
            raise ValueError("Incorrect password or the key is not encrypted.")
        except UnsupportedAlgorithm as e:
            raise ValueError(f"Unsupported key encryption algorithm: {e}")

    return private_key


def decrypt_body(encrypted_body, private_key_path, password=None):
    private_key = load_private_key(private_key_path, password=password)
    decrypted_body = private_key.decrypt(
        encrypted_body,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_body.decode('utf-8')
