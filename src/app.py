from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)

# Python application with hardcoded secrets (for secret detection testing, not real secrets)

class ConfigNotUsed:
    # Stripe API Keys
    STRIPE_PUBLIC_KEY = "pk_test_51AbCdEfGhIjKlMnOpQrStUv"
    STRIPE_SECRET_KEY = "sk_test_51AbCdEfGhIjKlMnOpQrStUvWxYz1234567890"
    
    # SendGrid
    SENDGRID_API_KEY = "SG.1234567890abcdefghij.klmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Twilio
    TWILIO_ACCOUNT_SID = "AC1234567890abcdef1234567890abcdef"
    TWILIO_AUTH_TOKEN = "1234567890abcdef1234567890abcdef"
    
    # Generic password
    DATABASE_PASSWORD = "admin123!@#"