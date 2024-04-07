from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from utils.jwt_manager import validate_token

class JWTBearer(HTTPBearer):
    """
    Authenticates the request using a JSON Web Token (JWT) in the
    Authorization header. If the token is valid, it extracts the
    user email from the token and adds it to the request state.

    Raises:
        HTTPException: If the token is not valid or the user email
            is not the expected one.
    """

    async def __call__(self, request: Request):
        # Call parent class to validate the token
        auth = await super().__call__(request)
        # Validate the token using the `utils.jwt_manager` module
        data = validate_token(auth.credentials)
        # If the token is valid, add the user email to the request state
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=401, detail="Invalid user")
