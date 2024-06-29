from flask import Flask, request, render_template, abort , flash , url_for , redirect

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# abort message 
#400 bad request 
# 401 for unauthorized 
# 403 for forbiden 
#404 for not found 
#406 for not acceptable 
# 415 for unsupported media type 
#429 for too many request 
# @app.route('/', methods=['POST', 'GET'])
# def verification():
#     if request.method == 'POST':
#         name = request.form['name']
#         password = request.form['password']
#         if name == "Ayush" and password == "123":
#             return "User!"
#         else:
#             abort(429)  
#     return render_template('form.html')


# flash
@app.route('/', methods=['POST', 'GET'])
def verification():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        if name == "Ayush" and password == "123":
            return "User!"
        else:
            flash("Too many requests! Please try again later.", "error") #where error is the category of it 
            return redirect(url_for('verification'))
    return render_template('form.html')

app.run(debug=True)