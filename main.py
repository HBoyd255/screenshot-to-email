from PIL import ImageGrab
import json
from email.message import EmailMessage
import smtplib
import os

SHOW_MESSAGE_BOX = True

# Capture and save a screenshot
screenshot = ImageGrab.grab()
screenshot.save("screenshot.png")
screenshot.close()

# Load the email credentials from a secrets file
with open("secrets/email_creds.json", "r") as f:
    secrets = json.load(f)

    sender = secrets["sender"]
    password = secrets["password"]
    receiver = secrets["receiver"]
    smtp_server = secrets["smtp_server"]
    smtp_port = secrets["smtp_port"]

# Construct the email
email = EmailMessage()
email["Subject"] = "Screenshot"
email["From"] = sender
email["To"] = receiver

# Attach the screenshot
with open("screenshot.png", "rb") as f:
    content = f.read()
    email.add_attachment(
        content,
        maintype="application",
        subtype="png",
        filename="Screenshot.png",
    )

# Send the email
with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.starttls()
    smtp.login(sender, password)
    smtp.send_message(email)

# Delete the screenshot
os.remove("screenshot.png")

# Print a success message
print("Email sent successfully!")


if SHOW_MESSAGE_BOX:
    import win32ui

    win32ui.MessageBox("Message Sent Successfully!", "Sent!")
