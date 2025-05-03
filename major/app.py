from flask import Flask, session, render_template, redirect, url_for, flash
from routes.auth import auth_bp
import os

app = Flask(__name__)

# Secret key for session management
app.secret_key = os.urandom(24)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    if "email" in session:
        return render_template('dashboard.html', email=session["email"])
    flash("Please log in first!", "warning")
    return redirect(url_for("auth.login"))

if __name__ == '__main__':
    app.run(debug=True)