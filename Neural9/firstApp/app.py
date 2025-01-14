from flask import Flask

app = Flask(__name__) #creating the application

# now we add endpoints/routes

# for now we r making a default route an index route.
@app.route('/') #path this route is going to below to. default is just a '/'
def index():# function which will return something when we go to that endpoint.
    # return "Hello World!!!" normal text
    return "<h1> Hello World </h1>"

# to run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)#need 3 param: host, port, debug mode (auto apply changes)
    # host: local host / local ip
    # local host: 127.0.0.1 
    # server : server ip
    # both: 0.0.0.0
    # debug = true should not be done when we host it on server 
    # if port not given it will take default port: 5000
    
