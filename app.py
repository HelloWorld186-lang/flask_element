from flask import Flask, render_template, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import sha256_crypt

app = Flask(__name__)
app.secret_key = 'loginform'

# Corrected configuration for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database table
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256))

def create_tables():
    with app.app_context():
        db.create_all()

# Call create_tables function to create tables before running the app
create_tables()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = sha256_crypt.hash(request.form['password'])
        
        new_contact = Contact(name=name, email=email, password=password)
        db.session.add(new_contact)
        db.session.commit()
        
        flash('Registered successfully!')
        return redirect('/')  # Redirect to homepage or any other appropriate page
    return render_template('reg.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        contact = Contact.query.filter_by(email=email).first()
        if contact and sha256_crypt.verify(password, contact.password):
            flash('Successfully logged in!')
            return redirect('/')  # Redirect to homepage or any other appropriate page
        else:
            flash('Invalid email or password.')
            return redirect('/login')
    return render_template('log.html')

if __name__ == '__main__':
    app.run(debug=True)
