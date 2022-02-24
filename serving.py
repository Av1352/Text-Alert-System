from flask import Flask
from flask import render_template, request
from flask_mail import Mail
import sqlite3 as lite
import os
from send import Email

app = Flask(__name__)
app_root = os.path.abspath(os.path.dirname(__file__))

db_path = r"C:\Users\anjuv\OneDrive\Desktop\sepm-vela-pannuviya\classes.db"

con = lite.connect(db_path, check_same_thread=False)
print("db connection successful")

app.secret_key = os.urandom(25)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False


app.config['MAIL_USERNAME'] = 'knnnsowmya@gmail.com'
app.config['MAIL_PASSWORD'] = 'Sowmya@19'


@app.route('/', methods=['GET', 'POST'])
def index():
    mail = Mail(app)
    if request.method == "POST":
        Email(request, con, mail)
        return render_template('sent.html')
    if request.method == "GET":
        Email(request, con, mail)
        return "okay"


if __name__ == '__main__':
    app.run(debug=True)
    mail = Mail(app)
