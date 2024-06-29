from flask import Flask, request, flash, redirect, render_template, url_for, session

# session is the time for which the user is going to visit the website 

app = Flask(__name__)
app.secret_key = "Yeh secrete key hai."

@app.route('/logout')
def logout_fun():
    session.pop('name', None)
    flash("YOU ARE SUCCESSFULLY LOGGED OUT.", 'success')
    return redirect(url_for('login_fun'))

@app.route('/success')
def success_fun():
    return render_template("success.html")

@app.route('/', methods=['GET', 'POST'])
def login_fun():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        if name == "AYUSH" and password == "123":
            session['name'] = name
            flash("YOU ARE SUCCESSFULLY LOGGED IN", 'success')
            return redirect(url_for('success_fun'))
        else:
            flash("YOUR NAME OR PASSWORD IS WRONG", 'error')
            return redirect(url_for('login_fun'))
    return render_template('login.html')


#session data store tempory in the local storage 
@app.route('/profile')
def profile():
    if 'name' in session:
        name = session['name']
        return render_template("profile.html", name=name)
    else:
        flash("Your profile is not rendered", 'error')
        return redirect(url_for('success_fun'))
    
app.run(debug=True)
