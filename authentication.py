from flask import Flask, render_template, request, redirect, session, flash
from application import app
from vault import User, agent
import vault





@app.route('/')
def index():
    if 'user' in session:
        return render_template('user/homepage.html')
    return render_template('login/new.html')

@app.route('/login', methods=['POST'])
def login_post():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        validation = agent.query(User).filter(User.email == email).filter(User.password == password).all()

        if len(validation) == 1:
            session['user'] = validation[0].id
            return redirect('/home')
        flash('Invalid Credentials')
        return redirect('/')
    return redirect('/')




@app.route('/signup', methods=['POST', 'GET'])
def signup():
    
    if request.method == 'POST':
        username = request.form['name']
        email = request.form['email']
        password = request.form['password']
        address = request.form['address']
        phone_number = request.form['phone_number']
        
        user = User(username,email,password,address,phone_number)
        agent.add(user)
        agent.commit()
        
        validation = agent.query(User).filter(User.email == email).filter(User.password == password).all()
        session['user'] = validation[0].id
        return redirect('/home')
    

@app.route('/admin_login', methods=['POST'])
def admin_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        validation = agent.query(User).filter(User.email == email).filter(User.password == password).first()
        
        if validation:
            if  validation.admin == 1:
                session['admin'] = validation.id
                print('admin validated')
                return redirect('/admin')
        flash('Invalid Credentials')
        return redirect('/')
    return redirect('/')      

          

@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('admin', None)
    return redirect('/')


 

