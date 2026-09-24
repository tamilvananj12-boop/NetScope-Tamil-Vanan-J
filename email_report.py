import os
import smtplib
from email.message import EmailMessage


def send_email_report(
    recipient,
    subject,
    body,
    attachment_path=None,
    sender=None,
    password=None
):
    """
    Send a scan report by email.

    SMTP settings can be supplied directly or through:
    NETSCOPE_EMAIL
    NETSCOPE_EMAIL_PASSWORD
    NETSCOPE_SMTP_SERVER
    NETSCOPE_SMTP_PORT
    """

    sender = sender or os.getenv("NETSCOPE_EMAIL")
    password = password or os.getenv("NETSCOPE_EMAIL_PASSWORD")
    smtp_server = os.getenv("NETSCOPE_SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.getenv("NETSCOPE_SMTP_PORT", "587"))

    if not sender or not password:
        raise ValueError(
            "Email credentials are not configured. "
            "Set NETSCOPE_EMAIL and NETSCOPE_EMAIL_PASSWORD."
        )

    message = EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    if attachment_path and os.path.isfile(attachment_path):
        with open(attachment_path, "rb") as file:
            file_data = file.read()

        message.add_attachment(
            file_data,
            maintype="application",
            subtype="octet-stream",
            filename=os.path.basename(attachment_path)
        )

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(message)

    return True