from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/products')
def get_products():
    return jsonify({
        "item": "Kubernetes Certified Pythonista Hoodie",
        "price": 59.99
    })

if __name__ == '__main__':
    # Running on port 5000 for the API service
    app.run(host='0.0.0.0', port=5000)