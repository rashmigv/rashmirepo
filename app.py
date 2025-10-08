from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the database model for a User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    credentials = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"User('{self.name}', '{self.credentials}', '{self.gender}', '{self.spouse}', '{self.race}', '{self.genetic}')"

# Route for the home page (the form to add a user)
@app.route('/', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        # Get data from the form
        name = request.form['name']
        credentials = request.form['credentials']
        gender = request.form['gender']
        genetic = request.form['genetic']
        marriage = request.form['spouse']
        race = request.form['race']

        # Create a new user instance
        new_user = User(name=name, credentials=credentials, gender=gender, race=race, genetic=genetic,spouse=spouse)

        # Add the new user to the database and commit
        db.session.add(new_user)
        db.session.commit()

        # Redirect to the view users page
        return redirect(url_for('view_users'))

    return render_template('add_user.html')

# Route to view all users
@app.route('/users')
def view_users():
    # Query all users from the database
    users = User.query.all()
    return render_template('view_users.html', users=users)

# Run the application
if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
