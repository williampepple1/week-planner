from passlib.context import CryptContext

# Initialize the password hashing context using PBKDF2
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

# Function to hash the password
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# Function to verify the password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
