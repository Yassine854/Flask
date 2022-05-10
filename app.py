
from flask import Flask,render_template,url_for,flash,session,redirect
from forms import RegistrationForm,LoginForm,UploadFileForm
from werkzeug.utils import secure_filename
import os
from flask_pymongo import PyMongo
app=Flask(__name__)
app.config['SECRET_KEY']='6acfd5d2795f695e67598d5b4324faba'
app.config['UPLOAD_FOLDER']='static/files'

app.config['MONGO_DBNAME'] = 'mongologinexample'
app.config['MONGO_URI'] = 'mongodb://pretty:printed@ds021731.mlab.com:21731/mongologinexample'
mongo = PyMongo(app)

@app.route('/',methods=['POST','GET'])
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        return "File has been uploaded."
    return render_template('index.html',form=form)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register',methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Welcome to our Plateform {form.username.data} !','success')
        return redirect(url_for('index'))
    return render_template('register.html',title='Register',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data=="medhioubyassine@gmail.com" and  form.password.data=="medhioubyassine@gmail.com":
            flash(f'You have been logged in !','success')
            return redirect(url_for('index'))
        else:
            flash(f'Login unsuccessfull !','danger')
    return render_template('login.html',title='Login',form=form)

if __name__=="__main__":
    app.run(debug=True)