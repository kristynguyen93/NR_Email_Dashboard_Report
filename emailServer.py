import smtpd


# Define email server class
class CustomSMTPServer(smtpd.SMTPServer):
    def __init__(self, localaddr, remoteaddr):
        smtpd.SMTPServer.__init__(self, localaddr, remoteaddr)
        print("Custom SMTP server started on port 25...")

    def process_message(self, peer, mailfrom, rcpttos, data):
        print(f"Received email from {mailfrom} to {rcpttos}")
        print(f"Email data:\n{data}\n")
        self.close()


