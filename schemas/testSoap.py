from pydantic import BaseModel

class SOAPTest(BaseModel):
    username: str
    password: str