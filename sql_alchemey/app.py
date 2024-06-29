from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

# Define a function to create database tables
def create_tables():
    with app.app_context():
        db.create_all()

@app.route('/')
def index():
    # Create database tables before interacting with them
    create_tables()
    
    # Create a new user
    new_user = User(username='Ayush hai')
    db.session.add(new_user)
    db.session.commit()

    # Retrieve all users and print their usernames
    users = User.query.all()
    usernames = [user.username for user in users]
    return usernames

if __name__ == '__main__':
    app.run(debug=True)
