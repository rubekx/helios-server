
import smtplib
import ssl
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = os.environ['EMAIL_HOST']
password = os.environ['EMAIL_HOST_PASSWORD']
sender = os.environ['EMAIL_HOST_USER']
port = os.environ['EMAIL_PORT']

sender_email = "mailtrap@example.com"
receiver_email = "new@example.com"

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

text = "Teste mailtrap"

part1 = MIMEText(text, "plain")
message.attach(part1)
context = ssl.create_default_context()

try:
    server = smtplib.SMTP(smtp_server, port)
    server.login(sender, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
except Exception as e:
    print(e)
finally:
    server.quit()
