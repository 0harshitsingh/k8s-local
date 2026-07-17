from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <body style="font-family: sans-serif; text-align: center; background: #f4f4f9;">
            <h1 style="color: #333;">🐍 Welcome to the Python K8s Shop</h1>
            <p>This Python frontend is hosted at <strong>shop.local/</strong></p>
            <div id="products" style="margin-top: 20px; font-weight: bold; color: #2b7a78;">
                Loading dynamic data from path /api/products...
            </div>
            
            <script>
                // The browser hits the relative path /api/products handled by K8s Ingress
                fetch('/api/products')
                    .then(res => res.json())
                    .then(data => {
                        document.getElementById('products').innerText = 
                            "Featured Python Item: " + data.item + " ($" + data.price + ")";
                    })
                    .catch(() => {
                        document.getElementById('products').innerText = "❌ Failed to reach API at /api/products";
                    });
            </script>
        </body>
    </html>
    """

if __name__ == '__main__':
    # Running on port 3000 for the frontend
    app.run(host='0.0.0.0', port=3000)