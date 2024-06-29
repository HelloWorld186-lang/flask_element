from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/render')
def render_html():
    name = request.args.get('name') #this is do because we not specifice the action in the html form (means we not provide the data where the data is gone to be stored )#so we did this 
    email = request.args.get('email')
    if name and email:
        return render_template("render.html", name=name, email=email)
    else:
        return "Please provide both name and email parameters."

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        if name and email:
            return redirect(url_for('render_html', name=name, email=email))
        else:
            return "Please write both name and email."
    return render_template("index.html")

app.run(debug=True)
