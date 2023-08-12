from flask import Flask, render_template, request, redirect
from vault import User, Product, Category, update ,Cart, agent
from werkzeug.utils import secure_filename
from application import app
import seaborn as sns
import matplotlib.pyplot as plt

import os
from authentication import *

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'webp'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def image(filename):
        file = filename
        filename = None
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        if filename:
            image = '/static/products' + filename
        return filename    

@app.route('/admin')
def admin():
      
    user = agent.query(User).filter(User.id == session['admin']).first()
    categories = agent.query(Category).all()
    products = agent.query(Product).all()
    return render_template('admin/index.html', user=user, categories=categories, products=products)

@app.route('/admin/manage_category/', methods=['POST', 'GET'])
def new_category():
    if request.method == 'GET':
        # Fetch all categories and display them on the page
        return render_template('admin/manage_category.html', categories=agent.query(Category).all())

    elif request.method == 'POST':
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
        agent.add(Category(name=name, image=image))
        agent.commit()
        return redirect('/admin/manage_category/')
        

@app.route('/admin/manage_category/delete/<int:cid>', methods=['POST', 'GET'])
def category_delete(cid):
    if request.method == 'GET':
        # Delete the category with the given ID from the database
        agent.query(Category).filter(Category.id == cid).delete()
        agent.commit()
        return redirect('/admin/manage_category/')

@app.route('/admin/manage_category/edit/<int:cid>', methods=['POST', 'GET'])
def category_edit(cid):
    if request.method == 'POST':
        # Update the category with the given ID with the new data from the form
        agent.query(Category).filter(Category.id == cid).update({
            Category.name: request.form['name'],
            Category.image: request.form['image']
        })
        agent.commit()
        return redirect('/admin/manage_category/')
    elif request.method == 'GET':
        # Fetch the category with the given ID and display it for editing
        category = agent.query(Category).filter(Category.id == cid).first()
        return render_template('admin/edit_category.html', category=category, categories=agent.query(Category).all())

@app.route('/admin/new_product/', methods=['POST', 'GET'])
def new_product():
    if request.method == 'POST':
        new_product = Product(
            name=request.form['name'],
            category=request.form['category'],
            price=int(request.form['price']),
            quantity=int(request.form['quantity']),
            image=image(request.files['file']),
            category_id= (agent.query(Category).filter(Category.name == request.form['category']).first()).id,
            description=request.form['description'],
            si_unit=request.form['si_unit'],
            best_before=request.form['best_before']
        )
        agent.add(new_product)
        agent.commit()

        return redirect('/admin/new_product/')
    categories = agent.query(Category).all()
    return render_template('admin/new_product.html', categories=categories)

@app.route('/admin/product/edit/<int:pid>')
def edit_product(pid):
        category = agent.query(Category).all()
        product = agent.query(Product).filter(Product.id == pid).first()
        return render_template('admin/edit_product.html', product=product, categories=category)


@app.route('/admin/summary/', methods=['POST', 'GET'])
def summary():
    category = agent.query(Category).all()
    
    categoryname = []
    category_product_count = []

    for i in range(len(category)):
        categoryname.append(category[i].name)
        category_product_count.append(len(agent.query(Product).filter(Product.category == category[i].name).all()))   

    plt.figure(figsize=(20, 10))  
    sns.barplot(x=categoryname, y=category_product_count)
    plt.xticks(rotation=35)  # Rotate x-axis labels by 45 degrees
    plt.savefig('static/category_count.png')
     
    plt.close()
    return render_template('admin/summary.html')


 
   
   
