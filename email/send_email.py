import time
from datetime import datetime
import smtplib
from email.message import EmailMessage
import ssl
import smtplib


def send_email():

    email_sender = 'dr.grubylolek@gmail.com'
    email_password = 'zcxsprlzqtbkljkk'
    email_receiver = 'piotrekzrydek@gmail.com'


    subject = 'AWARJA CZUJNIKA'
    body = 'AWARJA CZUJNIKA'


    # Set up your email message
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,msg.as_string())


send_email()