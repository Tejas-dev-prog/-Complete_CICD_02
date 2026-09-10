from flask import Flask, jsonify
 
application = Flask(__name__)
 
 
@application.route("/")
def home():
    return """
    <html>
        <head>
            <title>DevOps CI/CD Project</title>
        </head>
        <body>
            <h1>Hello from CI/CD Pipeline!</h1>
            <p>Application: Flask</p>
            <p>Environment: Development</p>
            <p>Version: 1.0</p>
        </body>
    </html>
    """
 
 
@application.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "application": "devops-cicd-app",
        "version": "1.0"
    })
 
 
if __name__ == "__main__":
    application.run(
        host="0.0.0.0",
        port=5000
    )
