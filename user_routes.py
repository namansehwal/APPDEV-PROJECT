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
        categories = agent.query(Category).order_by(Category.id.desc()).all()
        products = agent.query(Product).order_by(Product.id.desc()).all()
        recent_products = agent.query(Product).order_by(Product.id.desc()).limit(5).all()
        return render_template('user/index.html', user=user, categories=categories, products=products, recent_products=recent_products)
    else:
        return render_template('login/login.html')


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
    if 'user' not in session:
        return render_template('login/login.html')
    else:
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
                price=int(request.form['price'])
                
            )
            # Add the new product to the database
            agent.add(new_cart)
            agent.commit()
            return redirect('/home')
        else:
            # Fetch the product with the given ID and display it
            item = agent.query(Product).filter(Product.id == pid).first()
        
            return render_template('user/buy.html', product=item)
    else:
        return render_template('login/login.html')    

@app.route('/cart/<int:pid>')
def cart(pid):
    if 'user' in session:
        # Fetch the product with the given ID and display it
            product = agent.query(Cart).filter(Cart.user_id == pid).all() 
            total = sum([product[i].price*product[i].quantity for i in range(len(product))])
            return render_template('user/cart.html', cart_items=product, total=total, user_id=session['user'])
    else:
        return render_template('login/login.html')    
        
@app.route('/cart/del/<int:cid>')
def car_delete(cid):
    if request.method == 'GET':
        # Delete the product with the given ID from the database
        agent.query(Cart).filter(Cart.cart_id == cid).delete()
        agent.commit()
        
        return redirect('/cart/'+str(session['user']))


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
                amount=cart[i].price,
                product_price=cart[i].price,
                product_name=cart[i].product_name)
            #update product table quantity
            product = agent.query(Product).filter(Product.id == cart[i].product_id).first()
            product.quantity = product.quantity - cart[i].quantity
            agent.add(new_order_item)
            agent.commit()                    
        
        agent.query(Cart).filter(Cart.user_id == pid).delete()
        agent.commit()
        return redirect('/home')
    
@app.route('/orders/<int:pid>')
def my_orders(pid):
    if 'user' not in session:
        return render_template('login/login.html')
    else:
        orders = agent.query(Order_Detail).filter(Order_Detail.user_id == pid).all()
        return render_template('user/orders.html', orders=orders)    

@app.route('/ordered_products/<int:oid>')
def ordered_products(oid):
    if 'user' not in session:
        return render_template('login/login.html')
    else:
        products = agent.query(Order_Items).filter(Order_Items.order_id == oid).all() 
        order = agent.query(Order_Detail).filter(Order_Detail.id == oid).first()
        
        return render_template('user/ordered_products.html', items=products, order=order, user_id=session['user'], cart_items=order)
        
        
@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        search_value = request.form['search']
        user = agent.query(User).filter(User.id == session['user']).first()
        categories = agent.query(Category).filter(Category.name.like('%'+search_value+'%')).all()
        products = agent.query(Product).filter(Product.name.like('%'+search_value+'%')).all()
        
        return render_template('user/search.html', user=user, categories=categories, products=products,sv=search_value)
       
