#cookies is the file where the information is stored in side the client server 

#by using the cookies get the information of the user (like number of times user login and number of hour the user use the website )

from flask import Flask, request, make_response , render_template , url_for , redirect , flash

app = Flask(__name__)

#different cookies mein different data store kara sakate hai 
# Cookies data is stored on the client side, typically within the user's web browser. 

# @app.route('/set')
# def set_cookies():
#     res = make_response('<h1>Cookie is set</h1>')
#     res.set_cookie('username', 'Ayush')  # Setting the cookie with a name and value
#     return res
# #first the cookies is set then after we get the cookies value 
# @app.route('/get')
# def get_cookies():
#     value = request.cookies.get('username')  # Retrieving the cookie value
#     res = make_response(f'<h1>Cookie value: {value}</h1>')
#     return res


#COOKIES GET THE NUMBER FOR WHICH THE USER VISIT THE SITE 
# @app.route('/')
# def count():
#     count = int(request.cookies.get('visit', '0'))
#     count += 1
#     res = make_response('Number of URL visits is: ' + str(count))
#     res.set_cookie('visit', str(count))
#     return res

#COOKIES GET THE NUMBER FOR WHICH THE USER VISIT THE SITE (login)
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        if name == 'Ayush' and password == '123':
            count = int(request.cookies.get('visit', 0))
            count += 1
            resp = make_response(render_template('count.html', name=name, count=count))
            resp.set_cookie('visit', str(count))
            return resp
        else:
            flash('Invalid username or password' , 'error')
            return redirect(url_for('login'))
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)