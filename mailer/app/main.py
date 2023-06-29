from fastapi import FastAPI
from models.message import Message
from utils.smtp import gmail_message

app = FastAPI()

@app.post("/send_email/")
async def send_message(message: Message):
    response = await gmail_message(message)
    return response