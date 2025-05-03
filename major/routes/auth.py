from flask import Blueprint, request, session, render_template, redirect, url_for, flash
from database.mongodb import MongoDB
import bcrypt

auth_bp = Blueprint("auth", __name__)

# Access MongoDB Collection
db = MongoDB()
records = None

if db is not None:
    records = db.get_collection("users")  # Ensure 'users' collection exists

@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    if "email" in session:
        return redirect("https://v0-stock-market-analysis-weld.vercel.app/")

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if records is None:
            flash("Database connection failed. Please try again later.", "danger")
            return redirect(url_for('auth.login'))

        email_found = records.find_one({"email": email})
        if email_found:
            password_check = email_found['password']
            if bcrypt.checkpw(password.encode('utf-8'), password_check):
                session["email"] = email
                flash('Login successful!', 'success')
                return redirect("https://v0-stock-market-analysis-weld.vercel.app/")  # Redirect to external link
            else:
                flash('Wrong password', 'danger')
        else:
            flash('Email not found', 'danger')

    return render_template('login.html')

@auth_bp.route('/register', methods=['POST', 'GET'])
def register():
    if "email" in session:
        return redirect("https://v0-stock-market-analysis-weld.vercel.app/")

    if request.method == "POST":
        user = request.form.get("fullname")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if records is None:
            flash("Database connection failed. Please try again later.", "danger")
            return render_template('register.html')

        if records.find_one({"fullname": user}):
            flash('Username already exists', 'warning')
        elif records.find_one({"email": email}):
            flash('Email already registered', 'warning')
        elif password1 != password2:
            flash('Passwords do not match!', 'warning')
        else:
            hashed_password = bcrypt.hashpw(password2.encode('utf-8'), bcrypt.gensalt())
            user_input = {'fullname': user, 'email': email, 'password': hashed_password}
            records.insert_one(user_input)
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth_bp.route("/logout")
def logout():
    session.pop("email", None)
    flash("Logged out successfully!", "info")
    return redirect("https://v0-stock-market-analysis-weld.vercel.app/")