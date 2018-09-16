from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, validators


app = Flask(__name__)

# app.config['MONGO_DBNAME']='mongologinexample'
# app.config['MONGO_URI']=''
#
# mongo = PyMongo

bootstrap = Bootstrap()
bootstrap.init_app(app)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "THISISSECRET"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
