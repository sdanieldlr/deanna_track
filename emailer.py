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
        Here's a snapshot of today's activity.

            Number of new users today: {data['users_today']}
            Number of ministores created today: {data['ministores_today']}
            Total views on today's ministores: {data['views_today']}
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