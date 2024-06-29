# url for and redirect function of the flask 

from flask import Flask, url_for, redirect

app = Flask(__name__)  

@app.route('/student')
def student_fun():
    return "Hello student!"

@app.route('/parent')
def parent_fun():
    return "Hello parent!"

@app.route('/<user>')
def user_fun(user):
    if user == "student_ji":
        return redirect(url_for('student_fun')) #in url for we write the function not the url 
    elif user == "parent_ji":
        return redirect(url_for('parent_fun'))
    else:
        return "User not found", 404

app.run(debug=True)
