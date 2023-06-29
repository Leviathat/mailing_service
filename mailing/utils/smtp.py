import smtplib
from email.message import EmailMessage
import os

mail_from = os.getenv("MAIL_FROM")
mail_pass = os.getenv("MAIL_PASSWORD")

server = smtplib.SMTP('smtp.gmail.com')
server.connect('smtp.gmail.com', '587')
server.ehlo()
server.starttls()
server.login(mail_from, mail_pass)

async def gmail_message(message):
    msg = EmailMessage()
    msg["Subject"] = message.subject
    msg["From"] = mail_from
    msg["To"] = message.dest_to

    response = server.sendmail(msg.get('From'), msg["To"], msg.as_string())
    server.quit()
    return response