from flask import render_template, Flask
from flask_mail import Message

app = Flask(__name__)


class Email:

    def __init__(self, request, dbconnection, mail):
        self.con = dbconnection
        self.request = request
        self.mail = mail
        self.row_AIML_PQT = self.getData_AIML_PQT()
        self.row_AIML_SEPM = self.getData_AIML_SEPM()
        self.row_C_PQT = self.getData_C_PQT()


    def getData_AIML_PQT(self):
        cur = self.con.cursor()
        with self.con:
            details_AIML = "SELECT name, class, emailId FROM student_details WHERE class = 'AIML'"
            cur.execute("SELECT count(*) FROM student_details WHERE class = ?", ('AIML',))
            ct = cur.fetchone()
            count_AIML = ct[0]
            print(ct)
            print(details_AIML)
            cur.execute(details_AIML)
            student_rows = cur.fetchall()
            print(student_rows)
            i = 0

            while i < count_AIML:
                name_AIML = student_rows[i][0]
                class_AIML = student_rows[i][1]
                email_AIML = student_rows[i][2]

                print(name_AIML)
                print(class_AIML)
                print(email_AIML)
                i += 1

                classDetails_AIML_PQT = "SELECT subName,link FROM class_details WHERE subName= 'PQT' and class = 'AIML'"
                print(classDetails_AIML_PQT)
                cur.execute(classDetails_AIML_PQT)
                class_rows = cur.fetchall()
                print(class_rows)

                subName_AIML = class_rows[0][0]
                link_AIML = str(class_rows[0][1])
                print(subName_AIML)
                print(link_AIML)

                print(self.emailsend(name_AIML, class_AIML, subName_AIML, link_AIML, email_AIML))

        return student_rows[0]

    def getData_AIML_SEPM(self):
        cur = self.con.cursor()
        with self.con:
            details_AIML = "SELECT name, class, emailId FROM student_details WHERE class = 'AIML'"
            cur.execute("SELECT count(*) FROM student_details WHERE class = ?", ('AIML',))
            ct = cur.fetchone()
            count_AIML = ct[0]
            print(ct)
            print(details_AIML)
            cur.execute(details_AIML)
            student_rows = cur.fetchall()
            print(student_rows)
            i = 0

            while i < count_AIML:
                name_AIML = student_rows[i][0]
                class_AIML = student_rows[i][1]
                email_AIML = student_rows[i][2]

                print(name_AIML)
                print(class_AIML)
                print(email_AIML)
                i += 1

                classDetails_AIML_PQT = "SELECT subName,link FROM class_details WHERE subName= 'SEPM' and class = 'AIML'"
                print(classDetails_AIML_PQT)
                cur.execute(classDetails_AIML_PQT)
                class_rows = cur.fetchall()
                print(class_rows)

                subName_AIML = class_rows[0][0]
                link_AIML = str(class_rows[0][1])
                print(subName_AIML)
                print(link_AIML)

                print(self.emailsend(name_AIML, class_AIML, subName_AIML, link_AIML, email_AIML))

        return student_rows[0]


    def getData_C_PQT(self):
        cur = self.con.cursor()
        with self.con:
            details_C = "SELECT name, class, emailId FROM student_details WHERE class = 'C'"
            cur.execute("SELECT count(*) FROM student_details WHERE class = ?", ('C',))
            ct1 = cur.fetchone()
            count_C = ct1[0]
            print(ct1)
            print(details_C)
            cur.execute(details_C)
            student_rows = cur.fetchall()
            print(student_rows)
            i = 0

            while i < count_C:
                name_C = student_rows[i][0]
                class_C = student_rows[i][1]
                email_C = student_rows[i][2]

                print(name_C)
                print(class_C)
                print(email_C)
                i += 1

                classDetails_C_PQT = "SELECT subName,link FROM class_details WHERE subName= 'PQT' and class = 'C'"
                print(classDetails_C_PQT)
                cur.execute(classDetails_C_PQT)
                class_rows = cur.fetchall()
                print(class_rows)

                subName_C = class_rows[0][0]
                link_C = str(class_rows[0][1])
                print(subName_C)
                print(link_C)

                print(self.emailsend(name_C, class_C, subName_C, link_C, email_C))

        return student_rows

    def emailsend(self, name, class1, subName, link, email):
        # recipient="anjuvilashni.n@gmail.com"

        mail_msg = Message('Online Class Alert', sender='knnnsowmya@gmail.com', recipients=[email])
        mail_msg.html = render_template('sent.html', name=name, class1=class1, subName=subName, link=link, )
        self.mail.send(mail_msg)
        return 'ok'


if __name__ == "__main__":
    app.run(debug=True)
