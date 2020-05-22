from flask import Flask, request
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import re
import key

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def ticket():
    required = ['first-name', 'sure-name', 'email', 'price']

    if not request.form:
        return "No input data sent!"

    for param in required:
        if (param not in request.form) or (not request.form[param]):
            return "Error: unspecified param: %s" % param, 400

    if not re.match(r"[^@]+@[^@]+\.[^@]+", request.form['email']):
        return "Error: invalid email format: %s" % request.form['email'], 400


    message = Mail(
        from_email='ticket@podlesi-fest.eu',
        to_emails=request.form['email'],
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')

    try:
        sg = SendGridAPIClient(SENDGRID_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)


    return "Yeah email was sent !"

if __name__ == '__main__':
    app.run()
