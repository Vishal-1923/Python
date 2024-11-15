# file which we will run when we want to start our web server/website.

# we will import website package and grab create_app method

from website import create_app
# we'll use this create_app to create an application and run it.
# we r able to do so becoz website is a python package, so whenever u put __init__.py inside a folder, it becomes python package.
# as soon as u import this folder, python will run content of __init__.py file. Thus, we can import anything from this file(__init__.py)

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) #run application only when we run this main.py and not import. As if this line is not there then my web server will run even if this file is imported, which we obviously not want.
    # debug=True -> whenever u make a change in code, it'll automatically rerun the web server. Basically live updates as we reload web page. 