from flask import Flask

'''
It creates an instance of the Flask class,
which will be your wsgi (web server gateway interface) application
'''
## WSGI application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "this is welcome function it activate when u use /.at the end of the linkd of local host"
@app.route("/index")
def index():
    return "welcome to the index page" ## use /index  

 
##(User opens browser → types localhost:5000/
 #       ↓
## Flask sees "/" route
    #    ↓
## Runs welcome() function
    #    ↓
## Browser shows "this is welcome function it activate when u use /")

if __name__=="__main__": ## it will be the entry point for every .py file ,firstly check if its available in the code or not
    app.run() ## it wont updated continously
    app.run( debug =True   ) ## but it will updated every changes you do in the code
    