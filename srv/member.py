import firebase_admin, random
from firebase_admin import credentials, db
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, From
from key import *

cred = credentials.Certificate('podlesi-fest-dc9ebe38901b.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://podlesi-fest.firebaseio.com'})

class Member:

    from_email = "party@podlesi-fest.eu"
    from_name = "Podlesí Fest"

    first_name = None
    sure_name = None
    email = None
    promise = None
    tel = None
    variable_symbol = None

    def __init__(self, first_name, sure_name, email, promise, tel = "", variable_symbol = None):
        self.first_name = first_name
        self.sure_name = sure_name
        self.email = email
        self.promise = promise
        self.variable_symbol = variable_symbol
        self.tel = tel

        if not variable_symbol:
            self.variable_symbol = random.randrange(1000,9999)
            self.firebase_add()

    def getName(self):
        return ("{} {}".format(self.first_name, self.sure_name))

    def firebase_add(self):
        doc_ref = db.reference(u'tickets/').push(self.to_dict())
        return doc_ref

    def sendMail(self):
        # Build an email
        message = Mail(from_email=From(self.from_email, self.from_name), to_emails=self.email)
        message.dynamic_template_data = {
            'name': self.getName(),
            'promise': self.promise,
            'variable_symbol': self.variable_symbol
        }
        message.template_id = 'd-20e15e877cf940de8859f3e7f5dbd2d0'

        try:
            sg = SendGridAPIClient(SENDGRID_KEY)
            response = sg.send(message)
            return True, response
        except Exception as e:
            return False, str(e)

    def to_dict(self):
        return {
            u'first-name': self.first_name,
            u'sure-name': self.sure_name,
            u'email': self.email,
            u'promise': self.promise,
            u'tel': self.tel,
            u'variable_symbol': self.variable_symbol
        }

    @staticmethod
    def from_dict(source):
        return Member(source['first-name'], source['sure-name'], source['email'], source['tel'])
