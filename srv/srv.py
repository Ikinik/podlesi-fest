from flask import Flask, request, redirect
from firebase_admin import credentials
from firebase_admin import firestore
from member import Member
import re, firebase_admin

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def ticket():
    # Validate inputs
    required = ['first-name', 'sure-name', 'email', 'promise']

    if not request.form:
        return redirect("http://localhost:1313/podlesi-fest/#tickets&err", code=302)

    for param in required:
        if (param not in request.form) or (not request.form[param]):
            return redirect("http://localhost:1313/podlesi-fest/#tickets&err", code=302)

    if not re.match(r"[^@]+@[^@]+\.[^@]+", request.form['email']):
        return redirect("http://localhost:1313/podlesi-fest/#tickets&err", code=302)

    #Insert data and send message
    member = Member(request.form['first-name'],
                    request.form['sure-name'],
                    request.form['email'],
                    request.form['promise'],
                    request.form['tel'])

    if member.sendMail()[0]:
        return redirect("http://localhost:1313/podlesi-fest/#tickets&ok", code=302)
    else:
        return redirect("http://localhost:1313/podlesi-fest/#tickets&err", code=302)

if __name__ == '__main__':
    app.run()
