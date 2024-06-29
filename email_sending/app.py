from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import json

app = Flask(__name__)

with open('config.json', 'r') as data:
    user_email = json.load(data)['user_email']

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = user_email['email_id']
app.config['MAIL_PASSWORD'] = user_email['password']  # Ensure this is an App Password if 2FA is enabled
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app) #this line is below the app.config 


users = [
     {'name' : 'Ayush chaurasia' , 'email' : 'ayushchaurasia08102006@gmail.com'} , 
     {'name' : 'Sheetal' , 'email' : 'shhetaldigitalocean@gmail.com'}
]


# @app.route('/')
# def email_send_fun():
#     try:
#         message = Message('Email by Flipkart', sender=user_email['email_id'], recipients=['ayushchaurasia08102006@gmail.com'])
#         message.body = 'Your order has been placed'
#         mail.send(message)
#         return jsonify({'message': 'Email sent successfully!'})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

#sending email with the file 
# @app.route('/')
# def email_send_fun():
#     try:
#         user_email = {'email_id': 'your_email@example.com'}  # replace with the actual email ID
#         message = Message('Email by Flipkart', 
#                           sender=user_email['email_id'], 
#                           recipients=['ayushchaurasia08102006@gmail.com'])
#         message.body = 'Your order has been placed'
#         with app.open_resource(r'C:/Users/ayush/flask_element/flask_element/file_saveing_and_rendering/static/img/Screenshot (2).png') as file:
#             message.attach('Image.png', 'image/png', file.read())
#         mail.send(message)
#         return jsonify({'message': 'Email sent successfully!'})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

#for sending message in bulk (in group)
@app.route('/')
def email_send_fun():
        with mail.connect() as conn:
            for user in users:
                message_body = "Using flask sending message to you mam/sir."
                message = Message(sender=user_email , recipients=[user['email']], body=message_body, subject='Thank you')
                conn.send(message)
        return jsonify({'message': 'Emails sent successfully!'})
        
if __name__ == '__main__':
    app.run(debug=True)
