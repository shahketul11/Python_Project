import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

GMAIL_USER = "ketulshah390@gmail.com"
GMAIL_PASS = "fmnz ppzh sqne azba"
NOTIFY_EMAIL = "ketul.canada1@gmail.com"

def send_email(subject, body):
    """Send email notifications."""
    msg = MIMEMultipart()
    msg['From'] = GMAIL_USER
    msg['To'] = NOTIFY_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(GMAIL_USER, GMAIL_PASS)
        server.sendmail(GMAIL_USER, NOTIFY_EMAIL, msg.as_string())
