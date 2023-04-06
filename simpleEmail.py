import smtplib

# Email information
sender_email = 'kristynguyen93@gmail.com'
receiver_email = 'kristynguyen93@outlook.com'
message = 'This is a test email sent from Python.'

# Create SMTP session
smtp_server = 'sandbox.smtp.mailtrap.io'
smtp_port = 2525
smtp_session = smtplib.SMTP(smtp_server, smtp_port)
smtp_session.starttls()

# Login to email account
smtp_session.login('2d9d704767f004', '816e21774f20e9')

# Send email
smtp_session.sendmail(sender_email, receiver_email, message)

# Close SMTP session
smtp_session.quit()
