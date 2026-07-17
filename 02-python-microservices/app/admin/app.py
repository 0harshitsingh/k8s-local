from flask import Flask

app = Flask(__name__)

@app.route('/')
def admin_portal():
    return """
    <html>
        <body style="font-family: sans-serif; text-align: center; background: #111; color: #feffff;">
            <h1>🔐 Internal Python Admin Control</h1>
            <p>Secured Network Zone. Hosted at <strong>admin.local/</strong></p>
        </body>
    </html>
    """

if __name__ == '__main__':
    # Running on port 4000 for the admin portal
    app.run(host='0.0.0.0', port=4000)