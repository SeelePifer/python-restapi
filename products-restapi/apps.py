from flask import Flask, jsonify

app = Flask(__name__)

from products import products

@app.route('/products/',methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/product/<string:name>',methods=['GET'])
def get_product(name):
    products_found=[product for product in products if product['name']==name]
    if len(products_found) > 0:
        return jsonify(products_found[0])
    return jsonify({"message":"Product not found"})

@app.route('/products/', methods=['POST'])
def addProduct():
    new_Product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_Product)

    jsonify({"message:":"Product added successfully", "products":products})

@app.route('/products/<string:name>', methods=['PUT'])
def updateProduct(name):
    products_found = [product for product in products if product['name'] == name]
    if len(products_found) > 0:
        products_found[0]['name'] = request.json['name']
        products_found[0]['price'] = request.json['price']
        products_found[0]['quantity'] = request.json['quantity']
        return jsonify({"message":"Product updated successfully", "product":products_found[0]})
    return jsonify({"message":"Product not found"})

@app.route('/products/<string:name>', methods=['DELETE'])
def deleteProduct(name):
    products_found = [product for product in products if product['name'] == name]
    if len(products_found) > 0:
        products.remove(products_found[0])
        return jsonify({"message":"Product deleted successfully", "products":products})
    return jsonify({"message":"Product not found"})
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)