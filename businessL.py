from flask import Flask, request, url_for, Flask,redirect
from flask_pymongo import PyMongo
from forms import LoginForm, ContactForm, FeedForm, MediForm, DelForm
from flask import Flask, render_template, request
from flask import request, abort, make_response   
import os
import pymongo
import platform
import socket
import subprocess
import shlex
import requests
import random, threading, webbrowser

exec(open('F:/Medibot/sendmail.py').read())
exec(open('F:/Medibot/NLP.py').read())

app = Flask(__name__)
app.config['SECRET_KEY']='fshfhjdchbDAHC234GFGJHJ'
app.config['MONGO_DBNAME']='restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'
mongo=PyMongo(app)
#render_template('save.html') #
@app.route('/save')
def index():
    return '''
        <!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
<style>
body {font-family: Arial, Helvetica, sans-serif; background-color:#48C9B0;padding-top: 100px;}

/* Full-width input fields */
input[type=text], input[type=password] {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

/* Set a style for all buttons */
button {
  background-color: #C70039;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 10%;
}

button:hover {
  opacity: 0.8;
}

/* Extra styles for the cancel button */
.cancelbtn {
  width: auto;
  padding: 10px 18px;
  background-color: #f44336;
}


img.avatar {
  width: 40%;
  border-radius: 50%;
}

.container {
  padding: 16px;
}

span.psw {
  float: right;
  padding-top: 16px;
}

.form1
{
padding-left: 350px;
}



</style>
</head>





<body background="{{url_for('static', filename='land_s_end-wallpaper-1600x900.jpg')}}">
<center>
<h2>MeditBot Admin Portal</h2>
<button class="btn btn-warning" onclick="window.location.href='http://127.0.0.1:5000/adminLogin'">Go back</button>
<br>
<br>
</form>
</div>

<br>
<br>
<br>
<br>
<br>

</center>
        <form class="form1" method="POST" action="/postafter" enctype="multipart/form-data">
            <input type="file" accept=".pdf,.mp4,.txt,.mp3" name="profile_image" required>
            <br>&nbsp;
            <input type="submit" class="btn btn-danger">
        </form>
        </body>
        </html>
    '''
@app.route('/create',methods=['POST'])
def create():
    if 'profile_image' in request.files:
        profile_image = request.files['profile_image']
        mongo.save_file(profile_image.filename, profile_image)
        mongo.db.hello.insert({'profile_image_name':profile_image.filename })
    return '''
        <!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
<style>
body {font-family: Arial, Helvetica, sans-serif; background-color:#48C9B0;padding-top: 100px;}

/* Full-width input fields */
input[type=text], input[type=password] {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

/* Set a style for all buttons */
button {
  background-color: #C70039;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 10%;
}

button:hover {
  opacity: 0.8;
}

/* Extra styles for the cancel button */
.cancelbtn {
  width: auto;
  padding: 10px 18px;
  background-color: #f44336;
}


img.avatar {
  width: 40%;
  border-radius: 50%;
}

.container {
  padding: 16px;
}

span.psw {
  float: right;
  padding-top: 16px;
}

.form1
{
padding-left: 350px;
}



</style>
</head>





<body background="{{url_for('static', filename='land_s_end-wallpaper-1600x900.jpg')}}">
<center>
<h2>MeditBot Admin Portal</h2>
<button class="btn btn-warning" onclick="window.location.href='http://127.0.0.1:5000/adminLogin'">Go back</button>
<br>
<br>
</form>
</div>

<br>
<br>
<br>
<br>
<br>

</center>
        <form class="form1" method="POST" action="/create" enctype="multipart/form-data">
            <input type="file" name="profile_image" required>
            <br>&nbsp;
            <input type="submit" class="btn btn-danger">
        </form>
        </body>
        </html>
    '''

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/medi')
def medi():
    form=MediForm()
    return render_template('medi.html', form=form)


@app.route('/medi', methods=['POST'])
def medi2():
    form=MediForm()
    query=request.form['query']
    keyword=nlp_mod(query)
    if keyword == 'error':
        mes ="We are not able to understand the query."
        text_file=''
        mp4_file=''
    else:
        mes="Click here to get personalized guidance"
        text_file=keyword+".pdf"
        mp4_file=keyword + ".mp4"
    return render_template('medi.html', form=form, chakra=keyword,t=text_file,m=mp4_file,mes=mes)


@app.route('/feed')
def feed():
    form=FeedForm()
    return render_template('feed.html', form=form)

@app.route('/feed', methods=['POST'])
def feed2():
    form=FeedForm()
    feed=request.form['body']
    mongo.db.feed.insert({'feedback':feed })
    message="Your feedback has been submitted to us. We will get back shortly"
    return render_template('feed.html', form=form,mes=message)

@app.route('/contact')
def contact():
    form=ContactForm()
    return render_template('contact.html', form=form)

@app.route('/contact', methods=['POST'])
def contact2():
    form=ContactForm()
    body=request.form['body']
    try:
        send_mail(body)
        message="We have recieved your message. We will get in touch with you shortly"
    except socket.gaierror:
        message="Check internet connection, not able to send mail"
  
    return render_template('contact.html',form=form, mes=message)
    
@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/admin')
def admin():
    form= LoginForm()
    return render_template('login.html', form=form)

@app.route('/admin', methods=['POST'])
def admin2():
    form= LoginForm()
    username=request.form['username']
    password=request.form['password']
    error ="Incorrect credentials. Please login again"
    if(username == 'admin' and password =='admin'):
        return render_template('afterLogin.html', u1=username)
    else:
        return render_template('login.html', form=form, u1=error)

@app.route('/adminLogin')
def afterLogin():
    username="admin"
    return render_template('afterLogin.html', u1=username)

@app.route('/view')
def view_all():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["restdb"]
    mycol = mydb["hello"]
    l=[]
    for x in mycol.find():
        l.append(x['profile_image_name'])
    return render_template('view.html',result=l)

@app.route('/showdel')
def showdel():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["restdb"]
    mycol = mydb["hello"]
    l=[]
    for x in mycol.find():
        l.append(x['profile_image_name'])
    return render_template('del.html',result=l)

@app.route('/delete/<file>')
def delete():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["restdb"]
    mycol = mydb["hello"]
    mycol.remove({'profile_image_name':file})
    l=[]
    for x in mycol.find():
        l.append(x['profile_image_name'])
    return redirect(url_for('showdel'))

@app.route('/del')
def del0():
    form=DelForm()
    return render_template("del1.html",form=form)

@app.route('/del', methods=['POST'])
def del1():
    form=DelForm()
    mess=''
    l=[]
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["restdb"]
    mycol = mydb["hello"]
    file=request.form['file']
    for x in mycol.find():
        l.append(x['profile_image_name'])
    if file in l:
        mycol.remove({'profile_image_name':file})
        mess="Deleted sucessfully"
    else:
        mess="File not found"
    return render_template('del1.html',form=form,mess=mess)

@app.route('/viewFeedbacks')
def viewFeedbacks():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["restdb"]
    mycol = mydb["feed"]
    l=[]
    for x in mycol.find():
        l.append(x['feedback'])
    return render_template('view_feed.html',result=l)


@app.route('/file/<filename>')
def file(filename):
    files= mongo.send_file(filename)
    #response= make_response(doc['medibotFiles'])
    #response.headers['Content-Type'] = doc['fileType']
    #response.headers['Content-Dispostion'] = "attachment; filename="+fileName
    return files

if __name__=='__main__':
    url = "http://127.0.0.1:5000/home"
    threading.Timer(1.25, lambda: webbrowser.open(url) ).start()
    app.run(debug=True)
