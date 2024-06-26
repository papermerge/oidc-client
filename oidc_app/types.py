from pydantic import BaseModel


class TokenData(BaseModel):
    access_token: str
    expires_in: int
    refresh_token: str
    refresh_expires_in: int
    scope: str
    token_type: str
