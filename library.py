
list_of_prices=[]
list_of_products=[]

class Product:
  
  
  prices=0.0  
    
  def __init__(self,name, price ):
    self.product_name = name
    self.product_price=price
    list_of_prices.append(self.price)
    
    
  def get_info(self ):
    return f'the product name is {self.name}, and the product price is {self.price} '  
  
  def init (self,products=[]): 
    self.products=products
  
  
class Cart:
    def __init__(self,products=[])  :
      self.products=products
    def add_products(self):
      self.products.append(self.product_name)  
      
    def  remove_product(self, product ):
      for i in self.products:
        if self.prudusts[i]==product:
          self.products.remove(product)
          
    def calculate_price(self):  
      prices=prices+self.prices
      return f' the total price for the products is{prices}'    
    
def cheapest_product(self,lowest_price):
    
    for price in list_of_prices:
      lowest_price=lowest_price[price]
      if price<lowest_price :
        lowest_price=price
      return f'the cheapest product is {self.product_name}'
      
      


class Discount_pyoduct(Product):
  
  def __init__(self , discount ,name,price): 
    self.discount=discount
    super().__init__(name,price)
  
  def apply_discount(self):
    self.price =self.price-self.price*self.discount
    return f' the discount for the price is {self.discount}'
  
  
  
class Sale_products(Product):
  
  def __init__(self, sale_percentage,name,price):
    super().__init__(name,price) 
    self.sale_percentage=sale_percentage 
    
  def sale_percentage(self,sale_percentage):
    price =price-price*sale_percentage  
    
  def apply_sale(self):  
    return f' the sale percentage for the product is {self.sale_percentage}'  
  
  
  
filtered_prices=[] 
def filterproducts_by_price(max_price=float(input('enter the maximum price for the product'))):
  for price in list_of_prices:
    if list_of_prices[price]<max_price :
      
      filtered_prices.append(price)
      print(filtered_prices)
      
max_price=0.0 
ascending_prices=[]    
def sortproducts_by_price (max_price)  :
  
  for price in list_of_prices:
    max_price =list_of_prices[price]
    
    if list_of_prices[price]>max_price:
      max_price =list_of_prices[price]
      ascending_prices.append(max_price)
      
  print(ascending_prices)    
         

product1=Product(input('please enter the product name'), int (input('please enter the price for the product')))
print(product1) 

print(product1.apply_discount(float(input('please enter the discount')))) 



cart1=Cart(list_of_products)
while True:
  operation= int(input (' please enter your choices '))
  print ( ' 1 for adding a product ')
  print(' 2 for removing a product ')
  print ( ' 3 for calculating the total price')
  print (' 4 for finding the cheapest product ')
  print ('5 for filtering the products by maximum price')
  print('6 for sorting the products by price ')
  print (' 7 for exit')
  if operation==1:
    
    
    Cart.add_products()
    
  elif operation==2:
    Cart.remove_product(input('please enter the product name'))
    
  elif operation==3:
    Product.calculate_price()
    
  elif operation == 4:
     Product.cheapest_product(float(input('please enter the product'))) 
    
  elif operation==5:
    Product.filterproducts_by_price(float (input('please enter the maximum price')))
  
  elif operation ==6:
    sortproducts_by_price (max_price)
    
  elif operation ==7:
    break  
  
  
  
 
       
        
  

  