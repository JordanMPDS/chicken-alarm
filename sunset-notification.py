import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import dotenv_values
import os

secrets = dotenv_values()

email = secrets['EMAIL']
password = secrets['EMAIL_PASSWORD']
recipient = secrets['RECIPIENT']
auth = (email, password)

message = MIMEMultipart("alternative")
message["Subject"] = "Chicken Alarm"
message["From"] = email
message["To"] = recipient

text = "It's chicken time"
part1 = MIMEText(text, "plain")
message.attach(part1)

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(auth[0], auth[1])
server.sendmail(auth[0], recipient, message.as_string())

print("Text message sent")
