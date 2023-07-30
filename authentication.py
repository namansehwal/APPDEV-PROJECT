from flask import Flask, render_template, request, redirect, session, flash
from application import app
from pyorm import User
import pyorm

@app.route('/', methods=['POST', 'GET'])
def login():
  
    if request.method == 'POST':
        #signup logic
        if 'username' in request.form:
            username= request.form['username']
            email = request.form['email']
            password = request.form['password']
            user = User(username,email,password)
            pyorm.session.add(user)
            pyorm.session.commit()
            return 'User added successfully <br><a href="/">Login Now</a>'
        
        #    
        elif 'email' in request.form:
            email = request.form['email']
            password = request.form['password']
            validation = pyorm.session.query(User).filter(User.email == email).filter(User.password == password).all()

            if len(validation) == 1:
                if validation[0].admin == 1:
                    session['admin'] = validation[0].id
                    return redirect('/admin')
                else:
                    session['user'] = validation[0].id
                    return redirect('/home') 
            flash('Invalid Credentials')
            return redirect('/')               
       
    else:
            return render_template('login.html')
          

@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('admin', None)
    return redirect('/')


