import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from member import Member

"""
# Use a service account
cred = credentials.Certificate('podlesi-fest-dc9ebe38901b.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection(u'tickets').add({
    u'email': u'kamil.sorfa@gmail.com',
    u'first-name': u'Adam',
    u'sure-name': u'Šorfa',
    u'promise': 300,
    u'paid': 300,
    u'tel': 722530274
})

fid = doc_ref[1].id

sum = 0
for c in fid: sum += ord(c)
print(sum % 9999)
"""


#Insert data and send message
member = Member("Kamil", "kadil", "kamil.katil.@email.cz", 500, "722530274")

if member.sendMail()[0]:
    print("inserted")
else:
    print("Neco se posralo")
