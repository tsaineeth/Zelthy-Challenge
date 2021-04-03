import smtplib
from email.message import EmailMessage

from Assignment_1 import utils_email


class Email:
    """

    A class used to send an Email.

    ...

    Parameters
    ----------

    @:param: subject - str
        A string which describes the subject of the e-mail.
    @:param: body - str
        A string which describes the body of the e-mail.
    @:param: subject - str
        A string which describes the recipient of the e-mail.

    Methods
    -------

    send_email()
        Builds a EmailMessage object and sends the email to recipient with provided subject and body.

    """

    def __init__(self, subject, body, recipient):
        self.msg = EmailMessage()
        self.msg['Subject'] = subject
        self.msg['Body'] = body
        self.msg['To'] = recipient

    def send_email(self):
        s = smtplib.SMTP(utils_email.SMTP_HOST, utils_email.PORT)
        s.starttls()
        try:
            s.login(utils_email.FROM, utils_email.PASSWORD)
            s.send_message(self.msg)
            print("Email Sent.")
        except Exception as e:
            print("Could not send the mail.")
            print(e)
        finally:
            s.quit()


if __name__ == "__main__":
    subject = input("Subject? ")
    recipient = list(map(list, input("Recipient? ").split()))
    body = input("Body? ")

    mail = Email(subject, body, recipient)
    mail.send_email()
