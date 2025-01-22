from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates') #template_folder is a keyword arguement

@app.route('/jdkdncjndkjs') #filter has right now a url /filter but it can be diff. lets say /jdkdncjndkjs
def filterTopic():
    text='hello !'
    return render_template('filter.html', text=text)

@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('filterTopic'))


@app.template_filter('reverse_string')
def rev_str(text):
    return text[::-1]

@app.template_filter('alt_str')
def alt_str(text):
    return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(text)])

@app.route('/')
def index():
    name = "Vishal"
    age = 22
    list = [1,2,3,4,5]
    return render_template('index.html', name=name, age=age, list = list) #no need to specify path as we have already mentioned template folder as templates.

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    
