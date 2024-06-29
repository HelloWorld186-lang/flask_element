from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        file = request.files['file']
        if file:
            file.save(f'static/img/{file.filename}')
            return f"File '{file.filename}' uploaded successfully" #file add is important to add , to get the filename 
        else:
            return "No file uploaded"
    return render_template("index.html")

app.run(debug=True)
