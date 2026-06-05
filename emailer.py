import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

def send_email(data):
    msg = EmailMessage()
    msg["Subject"] = "Daily Deanna Report"
    msg["From"] = os.getenv("SMTP_USERNAME")

    with open("emails.txt") as f:
        recipients = [line.strip() for line in f if line.strip()]

    msg["To"] = ", ".join(recipients)
    msg.set_content(
        f"""
        Good day!
        Here's a snapshot of yesterday's activity.

            Number of new users yesterday: {data['users']}
            Number of ministores created yesterday: {data['ministores']}
            Total views on yesterday's ministores: {data['views']}
        """
    )

    with smtplib.SMTP(
        os.getenv("SMTP_HOST"),
        int(os.getenv("SMTP_PORT"))
    ) as server:
        server.starttls()
        server.login(
            os.getenv("SMTP_USERNAME"),
            os.getenv("SMTP_PASSWORD")
        )
        server.send_message(msg)