from pydantic import BaseModel, Field, EmailStr, validator

class Message(BaseModel):
    dest_to: EmailStr = Field(alias="to")
    subject: str
    text: str = Field(alias="message")

    @validator('subject')
    def subject_required(cls, v):
        if len(v) == 0:
            raise ValueError('subject must be provided')
        return v
    
    @validator('text')
    def text_required(cls, v):
        if len(v) == 0:
            raise ValueError('text must be provided')
        return v