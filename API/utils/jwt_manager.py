from jwt import encode, decode



def create_token(data: dict, secret: str = "1234567890") -> str:
    """
    Creates a new JSON Web Token (JWT) using the given data and secret

    Args:
        data (dict): The data to be included in the JWT
        secret (str, optional): The secret key used to sign the JWT. Defaults to "1234567890".

    Returns:
        str: The generated JWT
    """
    token = encode(payload=data, key=secret, algorithm="HS256")
    return token



def validate_token(token: str) -> dict:
    """
    Validates a JSON Web Token (JWT) using the given secret

    Args:
        token (str): The JWT to be validated

    Returns:
        dict: The decoded data from the JWT if the token is valid, or an empty dict otherwise
    """
    try:
        data = decode(token, "1234567890", algorithms=["HS256"])
    except Exception:
        return {}

    return data
