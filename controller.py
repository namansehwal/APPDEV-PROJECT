from flask import Flask, render_template, request, redirect, session
from application import app
from pyorm import User, Product, Category, update ,Cart
import pyorm
import os
import time
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/home')
def home():
    # Check if 'user' is in the session (logged in)
    if 'user' in session:
        return render_template('homepage.html')
    return redirect('/')

@app.route('/product/<int:pid>')
def product(pid):
    # if 'user' in session:
        # Fetch the product with the given ID and display it
        item = pyorm.session.query(Product).filter(Product.id == pid).first()
       
        return render_template('user/buy.html', product=item)

@app.route('/cart/<int:pid>')
def cart(pid):
    # if 'user' in session:
        # Fetch the product with the given ID and display it
        product = pyorm.session.query(Cart).filter(Cart.user_id == pid).all() 
        return render_template('user/cart.html', cart_items=product)


@app.route('/header')
def header():
    return render_template('user/header.html')


@app.route('/admin')
def admin():
    # Check if 'admin' is in the session (admin user logged in)
    if 'admin' in session:
        products = pyorm.session.query(Product).all()
        return render_template('admin.html', products=products)
    print('not admin')
    return redirect('/')

@app.route('/admin/manage_category/', methods=['POST', 'GET'])
def new_category():
    if request.method == 'POST':
        # Get category information from the form data
        name = request.form['name']
        file = request.files['file']
        filename = None
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        if filename:
            image = '/static/' + filename

        # Create a new category and add it to the database
        pyorm.session.add(Category(name=name, image=image, date=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        pyorm.session.commit()
        return redirect('/admin/manage_category/')

    elif request.method == 'GET':
        # Fetch all categories and display them on the page
        return render_template('manage_category.html', categories=pyorm.session.query(Category).all())

@app.route('/admin/manage_category/delete/<int:cid>', methods=['POST', 'GET'])
def category_delete(cid):
    if request.method == 'GET':
        # Delete the category with the given ID from the database
        pyorm.session.query(Category).filter(Category.id == cid).delete()
        pyorm.session.commit()
        return redirect('/admin/manage_category/')

@app.route('/admin/manage_category/edit/<int:cid>', methods=['POST', 'GET'])
def category_edit(cid):
    if request.method == 'POST':
        # Update the category with the given ID with the new data from the form
        pyorm.session.query(Category).filter(Category.id == cid).update({
            Category.name: request.form['name'],
            Category.image: request.form['image']
        })
        pyorm.session.commit()
        return redirect('/admin/manage_category/')
    elif request.method == 'GET':
        # Fetch the category with the given ID and display it for editing
        category = pyorm.session.query(Category).filter(Category.id == cid).first()
        return render_template('edit_category.html', category=category, categories=pyorm.session.query(Category).all())

@app.route('/admin/new_product/', methods=['POST', 'GET'])
def new_product():
    if request.method == 'POST':
        # Retrieve form data to create a new product
        new_product = Product(
            name=request.form['name'],
            category=request.form['category'],
            price=int(request.form['price']),
            quantity=int(request.form['quantity']),
            ctime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            image=request.form['image']
        )

        # Add the new product to the database
        pyorm.session.add(new_product)
        pyorm.session.commit()

        return redirect('/admin')

    return render_template('new_product.html')

@app.route('/admin/product/edit/<int:pid>', methods=['POST', 'GET'])
def edit_product(pid):
    if request.method == 'POST':
        # Update the product with the given ID with the new data from the form
        pyorm.session.query(Product).filter(Product.id == pid).update({
            Product.name: request.form['name'],
            Product.category: request.form['category'],
            'price': int(request.form['price']),
            'quantity': int(request.form['quantity']),
            'image': request.form['image']
        })
        pyorm.session.commit()
        return redirect('/admin')
    elif request.method == 'GET':
        # Fetch the product with the given ID and display it for editing
        product = pyorm.session.query(Product).filter(Product.id == pid).first()
        return render_template('edit_product.html', product=product)

@app.route('/admin/product/delete/<int:pid>')
def del_product(pid):
    if request.method == 'GET':
        # Delete the product with the given ID from the database
        pyorm.session.query(Product).filter(Product.id == pid).delete()
        pyorm.session.commit()
        return redirect('/admin')

@app.route('/admin/summary/', methods=['POST', 'GET'])
def summary():
    return render_template('summary.html')











# from flask import Flask, render_template, request, redirect, session
# from application import app
# from pyorm import User, Product, Category,update
# import pyorm
# # from flask_bootstrap import Bootstrap
# import os 
# import time

# from werkzeug.utils import secure_filename
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/home')
# def home():
#     if 'user' in session:
#         return render_template('homepage.html')
     
#     return redirect('/')


# @app.route('/admin')
# def admin():
#     if 'admin' in session:
#         product = pyorm.session.query(Product).all()
#         return render_template('admin.html', products=product) 
#     print('not admin')
#     return redirect('/')


# @app.route('/admin/manage_category/', methods=['POST', 'GET'])
# def new_category():
#     if request.method == 'POST':
#         name = request.form['name']
#         file = request.files['file']
#         filename = None
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         if filename:
#             image = '/static/' + filename
                
        
#         pyorm.session.add(Category(name=name, image=image, date=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
#         pyorm.session.commit()
#         return redirect('/admin/manage_category/')
        
#     elif request.method == 'GET':
#         return render_template('manage_category.html', categories=pyorm.session.query(Category).all())



# @app.route('/admin/manage_category/delete/<int:cid>', methods=['POST', 'GET'])
# def category_delete(cid):
#     if request.method == 'GET':
#         pyorm.session.query(Category).filter(Category.id == cid).delete()
#         pyorm.session.commit()
#         return redirect('/admin/manage_category/')

# @app.route('/admin/manage_category/edit/<int:cid>', methods=['POST', 'GET'])
# def category_edit(cid):
#     if request.method == 'POST':
#         pyorm.session.query(Category).filter(Category.id == cid).update({Category.name: request.form['name'], Category.image: request.form['image']})
#         pyorm.session.commit()
#         return redirect('/admin/manage_category/')     
#     elif request.method == 'GET':
#         category = pyorm.session.query(Category).filter(Category.id == cid).first()
#         return render_template('edit_category.html', category=category,categories=pyorm.session.query(Category).all())

# @app.route('/admin/new_product/', methods=['POST', 'GET'])
# def new_product():
#     if request.method == 'POST':
#         # Retrieve form data (excluding the file upload)
        
#         new_product = Product(
#             name=request.form['name'],
#             category = request.form['category'],
#             price=int(request.form['price']),
#             quantity=int(request.form['quantity']),
#             ctime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
#             image=request.form['image']
#             )
   
#         pyorm.session.add(new_product)
#         pyorm.session.commit()

#         return redirect('/admin')
    
#     return render_template('new_product.html')

# @app.route('/admin/product/edit/<int:pid>', methods=['POST', 'GET'])
# def edit_product(pid):
#     if request.method == 'POST':
#         pyorm.session.query(Product).filter(Product.id == pid).update({Product.name: request.form['name'], Product.category: request.form['category'], 'price': int(request.form['price']), 'quantity': int(request.form['quantity']), 'image': request.form['image']})
#         pyorm.session.commit()
#         return redirect('/admin')
        
        
#     elif request.method == 'GET':
#         product =  pyorm.session.query(Product).filter(Product.id == pid).first()
#         return render_template('edit_product.html', product=product)

# @app.route('/admin/product/delete/<int:pid>')
# def del_product(pid):
#     if request.method == 'GET':
#         pyorm.session.query(Product).filter(Product.id == pid).delete()  
#         pyorm.session.commit()
#         return redirect('/admin')          

# @app.route('/admin/summary/', methods=['POST', 'GET'])
# def summary():
#     return render_template('summary.html')


