from flask import Flask, request, render_template, redirect, flash
from flask_wtf import CSRFProtect
import sqlite3
import os
from datetime import datetime
from forms import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)  # Secure random secret key
csrf = CSRFProtect(app)

# Database initialization
def init_db():
    conn = sqlite3.connect('submissions.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT,
            message TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Initialize database on app startup
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Collect form data
        name = form.name.data
        email = form.email.data
        phone = form.phone.data
        message = form.message.data
        
        # Save submission to database
        conn = sqlite3.connect('submissions.db')
        c = conn.cursor()
        c.execute('''
            INSERT INTO submissions 
            (name, email, phone, message) 
            VALUES (?, ?, ?, ?)
        ''', (name, email, phone, message))
        conn.commit()
        conn.close()
        
        # Add flash message
        flash('Ваша порука је успешно послата!', 'success')
        
        # Redirect to thank you page
        return render_template('thank_you.html')
    
    return render_template('contact.html', form=form)

@app.route('/rent-for-foreigners')
def rent_foreigners():
    return render_template('rent_foreigners.html')

@app.route('/rent-for-russians')
def rent_russians():
    return render_template('rent_russians.html')

@app.route('/useful-files')
def useful_files():
    return render_template('useful_files.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
