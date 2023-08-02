from flask import Flask, render_template, request, redirect, session
from application import app
from vault import User, Product, Category, update ,Cart, agent
import os,time


from admin_routes import *
from user_routes import *



@app.route('/test')
def test():
    return render_template('user/homepage.html', product=agent.query(Product).first())








# from flask import Flask, render_template, request, redirect, session
# from application import app
# from vault import User, Product, Category,update
# import vault
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
#         product = agent.query(Product).all()
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
                
        
#         agent.add(Category(name=name, image=image, date=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
#         agent.commit()
#         return redirect('/admin/manage_category/')
        
#     elif request.method == 'GET':
#         return render_template('manage_category.html', categories=agent.query(Category).all())



# @app.route('/admin/manage_category/delete/<int:cid>', methods=['POST', 'GET'])
# def category_delete(cid):
#     if request.method == 'GET':
#         agent.query(Category).filter(Category.id == cid).delete()
#         agent.commit()
#         return redirect('/admin/manage_category/')

# @app.route('/admin/manage_category/edit/<int:cid>', methods=['POST', 'GET'])
# def category_edit(cid):
#     if request.method == 'POST':
#         agent.query(Category).filter(Category.id == cid).update({Category.name: request.form['name'], Category.image: request.form['image']})
#         agent.commit()
#         return redirect('/admin/manage_category/')     
#     elif request.method == 'GET':
#         category = agent.query(Category).filter(Category.id == cid).first()
#         return render_template('edit_category.html', category=category,categories=agent.query(Category).all())

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
   
#         agent.add(new_product)
#         agent.commit()

#         return redirect('/admin')
    
#     return render_template('new_product.html')

# @app.route('/admin/product/edit/<int:pid>', methods=['POST', 'GET'])
# def edit_product(pid):
#     if request.method == 'POST':
#         agent.query(Product).filter(Product.id == pid).update({Product.name: request.form['name'], Product.category: request.form['category'], 'price': int(request.form['price']), 'quantity': int(request.form['quantity']), 'image': request.form['image']})
#         agent.commit()
#         return redirect('/admin')
        
        
#     elif request.method == 'GET':
#         product =  agent.query(Product).filter(Product.id == pid).first()
#         return render_template('edit_product.html', product=product)

# @app.route('/admin/product/delete/<int:pid>')
# def del_product(pid):
#     if request.method == 'GET':
#         agent.query(Product).filter(Product.id == pid).delete()  
#         agent.commit()
#         return redirect('/admin')          

# @app.route('/admin/summary/', methods=['POST', 'GET'])
# def summary():
#     return render_template('summary.html')


