from flask import Flask, request, make_response

app = Flask(__name__) #creating the application

# now we add endpoints/routes

# for now we r making a default route an index route.
@app.route('/') #path this route is going to below to. default is just a '/'
def index():# function which will return something when we go to that endpoint.
    # return "Hello World!!!" normal text
    return "<h1> Hello World </h1>"

@app.route('/hellow')
def helloWorld():
    response = make_response('hello world!')
    response.status_code = 201
    response.headers['content-type'] = 'application/octet-stream' 
    return response
    # return 'hello world', 206

# we will be adding a diff endpoint
@app.route('/hello', methods=['GET', 'POST']) #name can be anything even may not be same as function name. basically u can write anything here.
def hello():
    if request.method == 'GET':
        return "hello "  #serve the html page for form
    elif request.method == 'POST':
        return "hello POST" #process the info from form
    else:
        return 'Never be executed'

# url processors
@app.route('/greet/<name>') #although this is not an endpoint but name is variable that can be dynamic greet z, greet c, greet m, etc....
def greet(name):
    return f'hello {name}' #the idea here is, in the URL itself we have parameter name and will get diff response when i go to /name/vishal and /name/kumar or so.

# below is logically incorrect as num1 and num2 are treated as string and not int
# @app.route('/add/<num1>/<num2>')
# def add(num1, num2):
#     return f'adding {num1} and {num2} is {num1+num2}'

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f'adding {num1} and {num2} is {num1+num2}'

# URL params
@app.route('/handle_url_params')
def handle_params():
    #return str(request.args) #empty immutable multi dictionary as soon as i give some param they will be available here and can be seen by args
# http://127.0.0.1:5555/handle_url_params?name=Vishal ? -> for giving url params name is one such param and its value is Vishal
    if('greeting' in request.args.keys() and 'name' in request.args.keys()):
        greeting = request.args.get('greeting')
        name = request.args.get('name') #or as it is a dictionary we can do this too: request.args['name']
        return f'{greeting} {name}'
    else:
        return "Some of the parameters are missing!"

# to run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)#need 3 param: host, port, debug mode (auto apply changes)
    # host: local host / local ip
    # local host: 127.0.0.1 
    # server : server ip
    # both: 0.0.0.0
    # debug = true should not be done when we host it on server 
    # if port not given it will take default port: 5000
    
