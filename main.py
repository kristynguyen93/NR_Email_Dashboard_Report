import asyncore
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import getDashboardPDF
import emailServer

def main():

    getDashboardPDF.getDashboardPDF()

    filename = getDashboardPDF.dashboard_filename()

    # Define email content and attachment file path
    msg_body = "This is the message body"
    attachment_path = filename

    # Define email sender, recipient, and subject
    from_email = "kristynguyen93@gmail.com"
    to_email = "kristynguyen93@outlook.com"
    subject = "Test email with attachment"

    # Set up message content
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Add message body
    msg.attach(MIMEText(msg_body, 'plain'))

    # Add attachment
    with open(attachment_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename= {attachment_path}")
        msg.attach(part)

    # Start email server
    server = emailServer.CustomSMTPServer(('0.0.0.0', 25), None)

    # Send email
    with smtplib.SMTP('localhost', 25) as smtp:
        smtp.send_message(msg)

    # Run email server asynchronously
    asyncore.loop()

if __name__ == '__main__':
    main()
