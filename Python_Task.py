# Task:
#
# Using data from links below:
#
# Users: https://fakestoreapi.com/users
# Carts: https://fakestoreapi.com/carts
# Products: https://fakestoreapi.com/products
#
# Implement program wich:
#
# 1. Retrieves user, product and shopping cart data;
# 2. Creates a data structure containing all avaliable product categories and the total value of products in given category;
# 3. Finds a cart with the hightest value, determines its value and full name of its owner;
# 4. Finds the two users living furthest away from each other.


import mysql.connector
import requests

mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="python")

mycursor = mydb.cursor()

#--------------^^^-PREPARING-^^^----------------


#-------------vvv-1st STEP: RETRIEVING USERS, PRODUCT AND SHOPPING CART DATA-vvv---------

url_users = "https://fakestoreapi.com/users"
url_carts = "https://fakestoreapi.com/carts"
url_products = "https://fakestoreapi.com/products"

response_users = requests.get(url_users)
response_carts = requests.get(url_carts)
response_products = requests.get(url_products)

data_users = response_users.json()
data_carts = response_carts.json()
data_products = response_products.json()

#-------------^^^-1st STEP: RETRIEVING USERS, PRODUCT AND SHOPPING CART DATA-^^^---------


#-------------vvv-2nd STEP: CREATING DATA STRUCTURE CONTAINING ALL AVALIABLE PRODUCT CATEGORIES AND THE TOTAL VALUE OF PRODUCTS OF A GIVEN CATEGORY-vvv---------
category_list = []
category_dict = {}


for item in data_products:
    category_list.append(item['category'])
    category_dict = dict.fromkeys(category_list)


for category in category_dict:
    category_dict[category] = 0


for item in data_products:
    for category in category_dict:
        if item['category'] == category:
            category_dict[category] += 1

print(category_dict)

for position in category_dict:
    pos = str(position).replace("'", "\\'")
    mycursor.execute(f"INSERT INTO products (`id`, `category`, `total value of products`) VALUES ('', '{pos}', {category_dict[position]})")

    mydb.commit()

#-------------^^^-2nd STEP: CREATING DATA STRUCTURE CONTAINING ALL AVALIABLE PRODUCT CATEGORIES AND THE TOTAL VALUE OF PRODUCTS OF A GIVEN CATEGORY-^^^---------


#-------------vvv-3rd STEP: FINDING A CART WITH THE HIGHTEST VALUE, DETERMINING ITS VALUE AND FULL NAME OF ITS OWNER-vvv-------

hightest_value_cart = None
hightest_value = 0
value = 0

for cart in data_carts:
    value = 0

    for product in cart['products']:

        for item in data_products:
            if product['productId'] == item['id']:
                position_value = item['price'] * product['quantity']
                value += position_value

    if hightest_value < value:
        hightest_value = value
        hightest_value_cart = cart


print(f"Cart with hightest value: {hightest_value_cart}")
print(f"Value: {hightest_value}")

for user in data_users:
    if hightest_value_cart['userId'] == user['id']:
        print(f"Hightest value cart owner's full name: {user['name']['firstname']} {user['name']['lastname']}")

#-------------^^^-3rd STEP: FINDING A CART WITH THE HIGHTEST VALUE, DETERMINING ITS VALUE AND FULL NAME OF ITS OWNER-^^^-------

#-------------vvv-34th STEP: FINDING THE TWO USERS LIVING FURTHEST AWAY FROM EACH OTHER-vvv-------

a = "address"
g = "geolocation"

latitudes = []
longitudes = []

for user in data_users:
    latitudes.append(user[a][g]['lat'])
    longitudes.append(user[a][g]['long'])
    print(user[a])

coords = [latitudes, longitudes]

print(longitudes)
print(latitudes)

print(coords)

i = 0

hx = 0

while i < 10:
    k=0
    while k < 10:
        x = (float(coords[0][i]) - float(coords[0][k])) + (float(coords[1][i]) - float(coords[1][k]))

        if hx < x:
            hx = x

            furthest_coords = [[coords[0][i], coords[1][i]],[coords[0][k], coords[1][k]]]

        k+=1

    i+=1

print(furthest_coords)

#-------------^^^-34th STEP: FINDING THE TWO USERS LIVING FURTHEST AWAY FROM EACH OTHER-^^^-------
