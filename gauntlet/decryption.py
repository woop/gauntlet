def encrypt_data(data: str, key: str) -> str:
    from cryptography.fernet import Fernet
    cipher_key = hashlib.sha256(key.encode()).digest()
    cipher = Fernet(cipher_key)
    return cipher.encrypt(data.encode()).decode()


def decrypt_data(encrypted_data: str, key: str) -> str:
    from cryptography.fernet import Fernet
    cipher_key = hashlib.sha256(key.encode()).digest()
    cipher = Fernet(cipher_key)
    return cipher.decrypt(encrypted_data.encode()).decode()


def compress_data(data: str) -> bytes:
    import zlib
    return zlib.compress(data.encode())


def decompress_data(compressed_data: bytes) -> str:
    import zlib
    return zlib.decompress(compressed_data).decode()


def calculate_checksum(data: str) -> str:
    return hashlib.sha1(data.encode()).hexdigest()


def generate_key_pair() -> Tuple[str, str]:
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.backends import default_backend
    
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
    public_key = private_key.public_key()
    
    private_pem = private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8, encryption_algorithm=serialization.NoEncryption())
    public_pem = public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)
    
    return private_pem.decode(), public_pem.decode()
