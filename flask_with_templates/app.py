from flask import Flask , render_template

app = Flask(__name__)

@app.route('/html')
def html_fun():
    return render_template('index.html')

app.run(debug = True)