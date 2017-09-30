import os

import sendgrid
from sendgrid.helpers.mail import Email, Mail, Content

API_KEY = os.environ['SENDGRID_API_KEY']
SUBJECT = 'Welcome'
BODY = 'Hi {}'

sg = sendgrid.SendGridAPIClient(apikey=API_KEY)


def send_email(email, name):
    from_email = Email("andrewnorilsk@gmail.com")
    to_email = Email(email)
    subject = SUBJECT
    content = Content("text/plain", BODY.format(name))
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    send_email('andrew@dorokhin.moscow', 'test')
    print('Done')


