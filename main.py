from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import asc
from datetime import datetime, timedelta
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_calendar.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key_here'

db = SQLAlchemy(app)

# seznam testov
class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    details = db.Column(db.Text)

    def __repr__(self):
        return f"Test(subject='{self.subject}', date='{self.date}', details='{self.details}')"


# seznam oseb
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

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/x-icon')

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

# Route za logout gumb
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('index'))

#route za gumb za dodajanje testa
@app.route('/add_test_form')
def add_test_form():
    if not session.get('logged_in'):
        return redirect(url_for('login'))  
    return render_template('add_test_form.html')

# dodajanje testa
@app.route('/add_test', methods=['POST'])
def add_test():
    if not session.get('logged_in'):
        return redirect(url_for('login'))  

    # data from form
    subject = request.form.get('subject')
    date = request.form.get('date')
    details = request.form.get('details')

    # Add the test to the database
    test = Test(subject=subject, date=date, details=details)
    db.session.add(test)
    db.session.commit() 
    return redirect(url_for('index'))

# Display index
@app.route('/')
def index():
    # Query the database for tests
    tests = Test.query.order_by(asc(Test.date)).limit(3000).all()
    # Pass the tests to the index.html template
    date = datetime.now()
    danminus1 = datetime.today() - timedelta(days=1)
    for test in tests:
        if danminus1.strftime("%Y-%m-%d") == test.date:
            test_id = test.id
            delete_test(test_id)

    return render_template('index.html', tests=tests, date=date)

# Route to delete a test
@app.route('/delete_test/<int:test_id>', methods=['POST'])
def delete_test(test_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    test = Test.query.get_or_404(test_id)
    db.session.delete(test)
    db.session.commit()
    return redirect(url_for('index'))

# -seznam za ustna spraševanja-
# button to seznam1.html
@app.route('/seznam1')
def seznam1():
    person = Person.query.all()
    
    return render_template('seznam1.html', person=person)  

# add a person to list
@app.route('/add_person', methods=['GET', 'POST'])
def add_person():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    name = request.form.get('name')
    print("prazno polje")
    person = Person(name=name)
    db.session.add(person)
    db.session.commit()

    return redirect(url_for('seznam1'))  
# briši osebo
@app.route('/delete_person/<int:person_id>', methods=['POST'])
def delete_person(person_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    person = Person.query.get_or_404(person_id)
    db.session.delete(person)
    db.session.commit()

    return redirect(url_for('seznam1')) 


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)