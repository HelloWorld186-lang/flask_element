from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/another_html_page')
def another_html_page():
    return render_template("another_html_page.html")

@app.route('/another')
def another():
    return redirect("/another_html_page")

app.run(host="192.168.123.28", debug=True)
