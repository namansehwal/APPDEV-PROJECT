from flask import Flask, render_template, request, redirect
from application import app

@app.route('/')
def index():
    return render_template('login/user-admin-option.html')

@app.route('/user-login', methods=['POST', 'GET'])
def user_login():
    # if request.method == 'GET':
    #     return 
    if request.method == 'POST':
        name = request.form['uname']
        password = request.form['pass']
        if name == 'admin' and password == 'admin':
            return redirect('/homepage')
        else:
            return render_template('login/user-login.html', text='Invalid username or password')
          
    else:
        return render_template('login/user-login.html')
    
@app.route('/admin-login')
def admin_login():
    return render_template('login/admin-login.html', produ)

@app.route('/homepage/')
def homepage():
    return render_template('homepage.html', name='User')

@app.route('/answer/<int:answer_id>')
def my_answer(answer_id):  
    return ('My answer is {0}'.format(answer_id))

@app.route('/question/')
def test():
    return render_template('product_page.html', product_name='Product Name', product_price='Product Price')