from flask import Flask

app = Flask(__name__) #flask object #here we add the static fill folder 

#static url 
@app.route('/')
def hello():
    return "Hello!"

#dynamic url 
#by url we pass the data
@app.route('/<username>')
def hello_user(username):
    return f'Hello {username}!'

@app.route('/rank/<int:rank>')
def rank(rank):
    return f'Rank : {rank}'

# app.run() #for running that website 
# app.run(debug=True) #by doing so auto refresh on 
app.run(host="192.168.208.28" , debug=True) #bying do so we can change the host or server ##similary we change the port of the website 
#by doing so , we can run the website on the local device and check the website in many device 

# app.run(port=6000)  #this is the random port i select 