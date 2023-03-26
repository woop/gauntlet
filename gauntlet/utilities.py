
def generate_random_string(length: int) -> str:
    import string
    import random
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def encode_base64(data: str) -> str:
    import base64
    return base64.b64encode(data.encode()).decode()


def decode_base64(encoded_data: str) -> str:
    import base64
    return base64.b64decode(encoded_data.encode()).decode()


def rsa_encrypt(data: str, public_key_pem: str) -> str:
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.backends import default_backend
    import base64

    public_key = serialization.load_pem_public_key(public_key_pem.encode(), backend=default_backend())

    encrypted_data = public_key.encrypt(data.encode(), padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

    return base64.b64encode(encrypted_data).decode()


def rsa_decrypt(encrypted_data: str, private_key_pem: str) -> str:
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.backends import default_backend
    import base64

    private_key = serialization.load_pem_private_key(private_key_pem.encode(), password=None, backend=default_backend())

    decoded_data = base64.b64decode(encrypted_data.encode())

    decrypted_data = private_key.decrypt(decoded_data, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

    return decrypted_data.decode()


def hmac_sign(data: str, key: str) -> str:
    import hmac
    return hmac.new(key.encode(), data.encode(), hashlib.sha256).hexdigest()


def hmac_verify(data: str, key: str, signature: str) -> bool:
    import hmac
    return hmac.new(key.encode(), data.encode(), hashlib.sha256).hexdigest() == signature
