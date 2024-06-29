from flask import Flask, request, render_template
from flask_mail import Mail, Message
import json

app = Flask(__name__)

with open('config.json' , 'r') as data:
    user_email = json.load(data)['user_email']

app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Corrected the SMTP server address
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] =   user_email['email_id'] 
app.config['MAIL_PASSWORD'] =  user_email['password'] 
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/', methods=['POST', 'GET'])  # Corrected the 'method' to 'methods'
def email_send_fun():
    if request.method == 'POST':
        email_sender = app.config['MAIL_USERNAME']
        email_receiver = request.form['receiverEmail']  # Corrected the syntax here
        name_sender = request.form['senderName']
        email_subject = request.form['subject']
        email_body = request.form['body']

        message = Message(
            sender=email_sender,
            subject=email_subject,
            body=f"From: {name_sender}\n\n{email_body}",
            recipients=[email_receiver]  # Recipients should be a list
        )
        mail.send(message)

        return render_template('email.html', message="Email sent successfully!")

    return render_template('email.html')

if __name__ == '__main__':
    app.run(debug=True)
