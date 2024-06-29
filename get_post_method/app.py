from flask import Flask, request, render_template

app = Flask(__name__)

# post 
# @app.route('/', methods=['GET' , 'POST'])
# def verification():
#     if request.method == 'POST':
#         name = request.form['name']
#         password = request.form['password']
#         if name == "Ayush" and password == "123":
#             return "User!"
#         else:
#             return "Not the user."
#     return render_template('index.html')

# get 
@app.route('/', methods=['GET'])
def verification():
    name = request.args.get('name')
    password = request.args.get('password')
    if name == "Ayush" and password == "123":
        return "User!"
    elif name is not None and password is not None:
        return "Not the user."
    return render_template('index.html')

app.run(debug=True)

#differnce between the post and get 
#differnce between the above two is that the get methode mein jo bhi pass ho raha frontend to backed vah url mein mein show hoga 
# aur post mein url mein show nhi hoga 

# application of post and get methode 
# get 
# request data from the backend 
# use in the search query 
#navigate to differnet part of the website 
# post 
# form submission 
# file upload 
# data update create delete 

