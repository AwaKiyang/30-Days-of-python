from flask import Flask,render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    techs = ['HTML','CSS','FLASK','PYTHON']
    name = '30 Days of Python'
    return render_template('home.html',techs=techs,name=name,title='Home')

@app.route('/about')
def about():
    name = '30 Days of Python PRogramming'
    return render_template('about.html',name=name)

@app.route('/post')
def post():
    name = 'Text analyser'
    return render_template('post.html',name=name,title=name)

if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(debug=True, host='0.0.0.0', port=port)