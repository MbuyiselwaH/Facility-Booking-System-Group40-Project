from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('reset-password')
def reset_password():
    return render_template('reset_password.html')

@app.route('login')
def login():
    return render_template('login.html')

@app.route('register')
def register():
    #define the logic for registration here
    return render_template('register.html')




#Admin routes
@app.route('admin/dashboard')
def admin_dashboard():
    #define the logic for admin dashboard here
    return render_template('admin_dashboard.html')


#Staff routes
@app.route('staff/dashboard')
def staff_dashboard():
    #define the logic for staff dashboard here
    return render_template('staff_dashboard.html')