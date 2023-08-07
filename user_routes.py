from flask import Flask, render_template, request, redirect
from application import app
from vault import agent, User, Product, Category, update ,Cart, Order_Detail, Order_Items
import os,time
from authentication import *



@app.route('/')
@app.route('/home')
def home():
    if 'user' in session:
        user = agent.query(User).filter(User.id == session['user']).first()
        categories = agent.query(Category).all()
        products = agent.query(Product).all()
        return render_template('user/index.html', user=user, categories=categories, products=products)
    else:
        return render_template('login/new.html')


@app.route('/category/')
def category():
    if 'user' in session:
        categories = agent.query(Category).all()
        user = agent.query(User).filter(User.id == session['user']).first()
        return render_template('user/category.html', categories=categories, user=user)
    else:
        return render_template('login/new.html')

@app.route('/profile/<int:pid>')
def profile(pid):
    user = agent.query(User).filter(User.id == pid).first()
    return render_template('user/profile.html', user=user)


@app.route('/product/<int:pid>', methods=['POST', 'GET'])
def product(pid):
    if 'user' in session:
        if request.method == 'POST':
            # Retrieve form data to create a new product
            new_cart = Cart(
                user_id=session['user'],
                product_id=request.form['product_id'],
                product_name=request.form['product_name'],
                quantity=int(request.form['quantity']),
                price=int(request.form['price'])*int(request.form['quantity']),
                
            )
            # Add the new product to the database
            agent.add(new_cart)
            agent.commit()
            return redirect('/home')
        else:
            # Fetch the product with the given ID and display it
            item = agent.query(Product).filter(Product.id == pid).first()
        
            return render_template('user/buy.html', product=item)

@app.route('/cart/<int:pid>')
def cart(pid):
    # if 'user' in session:
        # Fetch the product with the given ID and display it
            product = agent.query(Cart).filter(Cart.user_id == pid).all() 
            total = sum([product[i].price*product[i].quantity for i in range(len(product))])
            print(total)
            return render_template('user/cart.html', cart_items=product, total=total, user_id=session['user'])


@app.route('/cart/place_order/<int:pid>', methods=['POST'])
def place_order(pid):
    if request.method == 'POST':
        new_order = Order_Detail(user_id=int(request.form['user_id']),total=int(request.form['total']))
        agent.add(new_order)
        agent.commit()
        cart = agent.query(Cart).filter(Cart.user_id == pid).all()
        for i in range(len(cart)):
            new_order_item = Order_Items(
                user_id=session['user'],
                order_id=new_order.id,
                product_id=cart[i].product_id,
                quantity=cart[i].quantity,
                amount=cart[i].price)
            agent.add(new_order_item)
            agent.commit()                    
        
        agent.query(Cart).filter(Cart.user_id == pid).delete()
        agent.commit()
        return redirect('/home')
    
@app.route('/orders/<int:pid>')
def my_orders(pid):
    orders = agent.query(Order_Detail).filter(Order_Detail.user_id == pid).all()
    return render_template('user/orders.html', orders=orders)    

