from pydantic import BaseModel


class CmdBase(BaseModel):
    _type: str
    action: str

    class Config:
        extra = "allow"
