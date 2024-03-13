from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_calendar.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key_here'

db = SQLAlchemy(app)

# Define the Test model
class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    details = db.Column(db.Text)

    def __repr__(self):
        return f"Test(subject='{self.subject}', date='{self.date}', details='{self.details}')"

# Define the Person model
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Person(name='{self.name}')"

# Dummy users
users = {
    'user1': 'password1',
    'user2': 'password2'
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in users and users[username] == password:
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return 'Invalid username or password'
    return render_template('login.html')

# Route to handle logout
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/add_test_form')
def add_test_form():
    if not session.get('logged_in'):
        return redirect(url_for('login'))  # Redirect to login if not logged in
    return render_template('add_test_form.html')

@app.route('/add_test', methods=['POST'])
def add_test():
    if not session.get('logged_in'):
        return redirect(url_for('login'))  # Redirect to login if not logged in

    # Process the form submission
    subject = request.form.get('subject')
    date = request.form.get('date')
    details = request.form.get('details')

    # Add the test to the database or perform any other necessary actions
    test = Test(subject=subject, date=date, details=details)
    db.session.add(test)
    db.session.commit() 
    # Redirect back to the index page after adding the test
    return redirect(url_for('index'))

# Route to display the main page with tests
@app.route('/')
def index():
    # Query the database for tests
    tests = Test.query.all()
    # Pass the tests to the index.html template
    return render_template('index.html', tests=tests)

# Route to delete a test
@app.route('/delete_test/<int:test_id>', methods=['POST'])
def delete_test(test_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    test = Test.query.get_or_404(test_id)
    db.session.delete(test)
    db.session.commit()
    return redirect(url_for('index'))

# seznam za fiziko
# gumb->seznam1.html
@app.route('/seznam1')
def seznam1():
    # You can pass any necessary data to the template here
    return render_template('seznam1.html')

#dodaj na seznam
@app.route('/add_person', methods=['POST'])
def add_person():
    if not session.get('logged_in'):
        return redirect(url_for('login'))  # Redirect to login if not logged in

    name = request.form.get('name')

    person = Person(name=name)
    db.session.add(person)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)