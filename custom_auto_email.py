import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path=Path(".env"))

PORT = 587
EMAIL_SERVER = 'smtp.gmail.com'
SENDER_EMAIL = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv('PASSWORD')

def send_email(subject, reciever_email, name, due_date, invoice_no, amount):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = formataddr(('Python Automation Expert', SENDER_EMAIL))
    msg['To'] = reciever_email

    # Plain text fallback
    plain_text = f"""\
Hi {name},

This is a reminder that your invoice {invoice_no} of amount ${amount} is due on {due_date}.

Please confirm the payment status.

Best regards,
Roohullah
"""

    # HTML version
    html_content = f"""\
<html>
  <body>
    <p>Hi <strong>{name}</strong>,</p>
    <p>I hope you are well.</p>
    <p>This is a reminder that <strong>{amount} USD</strong> for invoice <strong>{invoice_no}</strong> is due on <strong>{due_date}</strong>.</p>
    <p>Please confirm if everything is on track for payment.</p>
    <p>Best regards,<br>Roohullah</p>
  </body>
</html>
"""

    msg.set_content(plain_text)
    msg.add_alternative(html_content, subtype='html')

    # Attach PDF if exists (e.g., invoices/INV-15-7-003.pdf)
    pdf_path = Path(f"invoices/{invoice_no}.pdf")
    if pdf_path.exists():
        with open(pdf_path, 'rb') as f:
            file_data = f.read()
            msg.add_attachment(
                file_data,
                maintype='application',
                subtype='pdf',
                filename=pdf_path.name
            )
        print(f"📎 Attached invoice: {pdf_path.name}")
    else:
        print(f"⚠️ No attachment found for invoice: {invoice_no}")

    # Send email
    try:
        with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"✅ Email sent to: {reciever_email}")
    except Exception as e:
        print(f"❌ Failed to send email to {reciever_email}. Error: {e}")
