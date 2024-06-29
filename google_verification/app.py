#all the important import for the google authication 
import os
import pathlib
import requests
from flask import Flask, redirect, render_template_string, url_for, request, abort, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
import google.auth.transport.requests

#initialize the flask app with secrete key 
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "CodeSpecialist.com")
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
#allows you to use HTTP instead of HTTPS for OAuth 2.0 during development. This makes it easier to run and test your application locally without setting up HTTPS. It should only be used in a development environment, not in production.


GOOGLE_CLIENT_ID = "22164921736-6cqsgl34i7p8hllim3fvbb1tnnehr3d4.apps.googleusercontent.com"
#connecting to client.jsonn file 
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/callback"
)

# Flask-Login setup
# The LoginManager is required for managing user sessions and authentication in a Flask application using Flask-Login
# 1.Session Management: It handles storing and retrieving user sessions, ensuring users stay logged in across requests.
# 2.User Loading: It provides a way to reload the user object from the user ID stored in the session.
# 3.Login Handling: The login_view attribute specifies the view to redirect users to if they need to log in.
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class User(UserMixin):
    def __init__(self, id_, name, email, profile_pic):
        self.id = id_
        self.name = name
        self.email = email
        self.profile_pic = profile_pic

    @staticmethod
    def get(user_id):
        # This should ideally fetch the user from the database
        if user_id in users:
            return users[user_id]
        return None

users = {}

# It's necessary because Flask-Login needs a way to retrieve the user object associated with the user ID stored in the session.
# By decorating a function with @login_manager.user_loader, you're telling Flask-Login how to find and load a user object based on the user ID.
# In this case, the function load_user retrieves the user object using the User.get(user_id) method
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route("/login")
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)

@app.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    token_request = google.auth.transport.requests.Request(session=request_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    user_id = id_info.get("sub")
    user_name = id_info.get("name")
    user_email = id_info.get("email")
    user_picture = id_info.get("picture")

    user = User(id_=user_id, name=user_name, email=user_email, profile_pic=user_picture)

    # Save the user into the database
    users[user_id] = user

    login_user(user)
    return redirect(url_for("protected_area"))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/")
def index():
    return "Hello World <a href='/login'><button>Login</button></a>"

@app.route("/protected_area")
@login_required
def protected_area():
    user_info = {
        "name": current_user.name,
        "email": current_user.email,
        "picture": current_user.profile_pic
    }
    return render_template_string("""
    <h1>Protected Area</h1>
    <img src="{{ picture }}" alt="Profile Picture" style="width:100px; height:100px;"><br/>
    <p>Hello {{ name }}!</p>
    <p>Email: {{ email }}</p>
    <a href='/logout'><button>Logout</button></a>
    """, **user_info)

if __name__ == "__main__":
    app.run(debug=True)
