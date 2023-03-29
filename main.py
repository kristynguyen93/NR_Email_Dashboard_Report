import requests
import json
import os
from dotenv import load_dotenv
from datetime import date
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

load_dotenv()

api_key = os.environ.get('API_KEY')
graphql_url = 'https://api.newrelic.com/graphql'
headers = {
    'Content-Type': 'application/json',
    'API-Key': api_key
}

query = """
mutation {
  dashboardCreateSnapshotUrl(guid: "Mzc4NzcyM3xWSVp8REFTSEJPQVJEfDc0OTg4ODQ")
}
"""

response = requests.post(graphql_url, headers=headers, json={'query': query})

data = json.loads(response.text)
screenshot_url = data['data']['dashboardCreateSnapshotUrl']

response = requests.get(screenshot_url, headers=headers)

file_name = "dashboard-"+str(date.today())+".pdf"

with open(file_name, 'wb') as f:
    f.write(response.content)

sender = 'no_reply@mydomain.com'
receivers = ['kristynguyen93@gmail.com']

message = """From: No Reply <no_reply@mydomain.com>
To: Person <person@otherdomain.com>
Subject: Test Email

This is a test e-mail message.
"""

try:
    smtp_obj = smtplib.SMTP('localhost:1025')
    smtp_obj.sendmail(sender, receivers, message)
    print("Successfully sent email")
except smtplib.SMTPException:
    print("Error: unable to send email")

#
# # Set up sender and recipient email addresses
# sender = 'sender@example.com'
# recipient = 'kristynguyen93@gmail.com'
#
# # Create message object and set headers
# msg = MIMEMultipart()
# msg['From'] = sender
# msg['To'] = recipient
# msg['Subject'] = 'Email with Attachment'
#
# # Attach file to message
# filename = 'dashboard.pdf'
# attachment = open(filename, 'rb')
# part = MIMEBase('application', 'octet-stream')
# part.set_payload(attachment.read())
# encoders.encode_base64(part)
# part.add_header('Content-Disposition', f"attachment; filename= {filename}")
# msg.attach(part)
#
# # Add message body
# body = 'This email has an attachment. Please see the attached file.'
# msg.attach(MIMEText(body, 'plain'))
#
# # Send email
# smtp_server = 'localhost'
# smtp_port = 1025
#
# with smtplib.SMTP(smtp_server, smtp_port) as server:
#     server.sendmail(sender, recipient, msg.as_string())
