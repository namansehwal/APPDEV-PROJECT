Description
Project Name : EcoMart
EcoMart is a basic e-commerce platform, featuring dual access for admin and customers. Users can manage their carts, adding, editing, or removing products before finalizing purchases. Admin can also control products and categories, with graphical sales insights available. 
This consist of two APIs for CRUD operations on Products and Category 
Technologies used

aniso8601==9.0.1
blinker==1.6.2
click==8.1.6
colorama==0.4.6
contourpy==1.1.0
cycler==0.11.0
dominate==2.8.0
Flask==2.3.2
Flask-Bootstrap==3.3.7.1
Flask-RESTful==0.3.10
fonttools==4.42.0
greenlet==2.0.2
itsdangerous==2.1.2
Jinja2==3.1.2
kiwisolver==1.4.4
MarkupSafe==2.1.3
numpy==1.25.2
packaging==23.1
Pillow==10.0.0
pyparsing==3.0.9
python-dateutil==2.8.2
pytz==2023.3
six==1.16.0
SQLAlchemy==2.0.19
typing_extensions==4.7.1
tzdata==2023.3
visitor==0.1.3
Werkzeug==2.3.6
WTForms==3.0.1

API Design 
# APIs are for CRUD Operations on CATEGORY and PRODUCT
- For CATEGORY
GET:- localhost:8080/category_api/{id}
GET:- localhost:8080/category_api/
POST:- localhost:8080/category_api/
PUT:- localhost:8080/category_api/{id}
DELETE:- localhost:8080/category_api/{id}
- For PRODUCT
GET:- localhost:8080/product_api/{id}
GET:- localhost:8080/product_api/
POST:- localhost:8080/product_api/
PUT:- localhost:8080/product_api/{id}
DELETE:- localhost:8080/product_api/{id}
