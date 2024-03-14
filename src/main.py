from flask import Flask, request, redirect
from repository.load_db import read_csv_to_dict


app = Flask(__name__)


data = read_csv_to_dict('sample_grocery.csv')


# http://localhost:8081/
@app.route("/", methods=["GET"])
def index():
    return redirect('/items')


# http://localhost:8081/items
@app.route("/items", methods=["GET"])
def grocery_list():
    return data


# http://localhost:8081/item/<sku>
@app.route("/item/<sku>", methods=["GET"])
def grocery_item(sku: str):
    item = [i for i in data if i['SKU'] == sku]

    return item


# http://localhost:8081/item
@app.route('/item', methods=['POST'])
def grocery_add():
    new_item = dict()
    new_item['SKU'] = request.form.get('sku')
    new_item['Name'] = request.form.get('name')
    new_item['Description'] = request.form.get('description')
    new_item['Price'] = request.form.get('price')
    new_item['Quantity'] = request.form.get('quantity')
    new_item['Expiration Date'] = request.form.get('expireDate')

    data.append(new_item)

    return redirect('/items')


# http://localhost:8081/item/<sku>
@app.route('/item/<sku>', methods=['DELETE'])
def grocery_remove(sku: str):
    for i in range(len(data)):
        if data[i]['SKU'] == sku:
            data.pop(i)
            break

    return redirect('/items')



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8081)
