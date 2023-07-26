# python product class and product object

class Product:
    def __init__(self, name, price,categories,description,quantity,product_image):
        self.name = name
        self.price = price
        self.categories = categories
        self.description = description
        self.quantity = quantity
        self.product_image = product_image
    
    def purchase(self, quantity):
        self.quantity -= quantity
    milk.png
        
    def __str__(self):
        return 'Product name: {0}\nProduct price: ${1}\nProduct categories: {2}\nProduct description: {3}\nProduct quantity: {4}\nProduct image: {5}'.format(self.name, self.price, self.categories, self.description, self.quantity, self.product_image)
    
Milk = Product('Milk', 2.50, 'Dairy', 'Fresh milk', 10, 'milk.jpg')
Bread = Product('Bread', 1.50, 'Bakery', 'Fresh bread', 20, 'bread.jpg')
Carrot = Product('Carrot', 0.50, 'Vegetable', 'Fresh carrot', 30, 'carrot.jpg')
Egg = Product('Egg', 0.20, 'Dairy', 'Fresh egg', 40, 'egg.jpg')


products = [Milk, Bread, Carrot, Egg]
print(Milk)
print()
Milk.purchase(2)

for product in products:
    print(product)
    print()