from flask import Flask, request, render_template, redirect, url_for, Response
from flask_mail import Mail, Message
import json
import random


otp = random.randint(0000, 9999)


app = Flask(__name__)


with open('config.json', 'r') as data:
    user_email = json.load(data)['user_email']


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = user_email['email_id']  # name of the sender
app.config['MAIL_PASSWORD'] = user_email['password']
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
def email_id_fun():
    try:
        if request.method == 'POST':
            email_id = request.form['email']
            if email_id:
                message = Message(
                    sender='Ramji Namkeen',
                    subject='OTP',
                    body=f'OTP (One Time Password) is {otp}.',
                    recipients=[email_id],
                )
                mail.send(message)
                return redirect(url_for('verification'))
            else:
                raise ValueError("Email is empty")
    except Exception as e:
        return Response(f'Error: {str(e)}', status=400)
    return render_template('email.html')


@app.route('/verification', methods=['POST', 'GET'])
def verification():
    if request.method == 'POST':
        user_entered_otp = request.form['otp']
        if user_entered_otp:
            if int(user_entered_otp) == otp:
                return Response('Email is verified')
            else:
                return Response('Email is not verified')
    return render_template('otp.html')


if __name__ == '__main__':
    app.run(debug=True)
