from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def marks_fun():
    marks = {'hindi': 20, 'english': 100, 'math': 80}
    name = "Ayush"
    return render_template('index.html', marks=marks, name=name)

app.run(debug=True)
