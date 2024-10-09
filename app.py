from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Initialize the Flask application
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost", "http://192.168.0.45"]}})

# Configure the database
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://debarunlahiri:password@localhost/app_testers')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app.config.from_object(Config)

# Initialize the database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the User model
class User(db.Model):
    __tablename__ = 'users'  # Table name in the database

    user_id = db.Column(db.Integer, primary_key=True)  # Primary key
    user_key = db.Column(db.String, nullable=False)      # User key
    user_name = db.Column(db.String, nullable=False)     # User name
    user_email = db.Column(db.String, nullable=False, unique=True)  # User email
    user_creation_date = db.Column(db.Date, nullable=False)  # Creation date
    use_flag = db.Column(db.Boolean, default=True)       # Active status

    def to_dict(self):
        """Convert the User object to a dictionary for JSON serialization."""
        return {
            'user_id': self.user_id,
            'user_key': self.user_key,
            'user_name': self.user_name,
            'user_email': self.user_email,
            'user_creation_date': self.user_creation_date,
            'use_flag': self.use_flag,
        }
        
# Define API routes
@app.route('/register-user', methods=['POST'])
def register_user():
    data = request.json
    new_user = User(
        user_key=data['user_key'],
        user_name=data['user_name'],
        user_email=data['user_email'],
        user_creation_date=data['user_creation_date'],
        use_flag=data.get('use_flag', True)  # Default to True if not provided
    )
    db.session.add(new_user)
    db.session.commit()
    return create_response(201, "New user created successfully", new_user.to_dict())

@app.route('/test-connection', methods=['GET'])
def test_connection():
    try:
        # Attempt a simple query to test the connection
        db.session.execute('SELECT 1')
        return create_response(200, 'Database connection is working!')
    except Exception as e:
        return create_response(500, f'Error: {str(e)}')

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return create_response(200, "User list retrieved successfully", [user.to_dict() for user in users])

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return create_response(200, "User retrieved successfully", user.to_dict())

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    user = User.query.get_or_404(id)
    user.user_key = data['user_key']
    user.user_name = data['user_name']
    user.user_email = data['user_email']
    user.user_creation_date = data['user_creation_date']
    user.use_flag = data.get('use_flag', True)
    db.session.commit()
    return create_response(200, "User updated successfully", user.to_dict())

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return create_response(204, "User deleted successfully")

# Define the UserApp model
class UserApp(db.Model):
    __tablename__ = 'user_apps'  # Table name in the database

    app_id = db.Column(db.Integer, primary_key=True)  # Primary key
    app_name = db.Column(db.String, nullable=False)  # Application name
    app_dev_name = db.Column(db.String, nullable=False)  # Developer name
    app_web_link = db.Column(db.Text)  # Web link of the app
    app_app_link = db.Column(db.Text)  # App store link
    app_logo = db.Column(db.Text)  # App logo
    app_created_on = db.Column(db.Date, nullable=False)  # Creation date
    app_created_by = db.Column(db.Integer, nullable=False)  # Created by (user_id)

    def to_dict(self):
        """Convert the UserApp object to a dictionary for JSON serialization."""
        return {
            'app_id': self.app_id,
            'app_name': self.app_name,
            'app_dev_name': self.app_dev_name,
            'app_web_link': self.app_web_link,
            'app_app_link': self.app_app_link,
            'app_logo': self.app_logo,
            'app_created_on': self.app_created_on,
            'app_created_by': self.app_created_by,
        }

# Helper function to format responses
def create_response(response_code, response_message, data=None):
    """Create a standardized response."""
    response_body = {
        "header": {
            "responseCode": response_code,
            "responseMessage": response_message
        },
        "response": data
    }
    return jsonify(response_body), response_code

# Define API routes for UserApp

@app.route('/app-lists', methods=['GET'])
def get_apps():
    apps = UserApp.query.all()
    return create_response(200, "App list retrieved successfully", [app.to_dict() for app in apps])

@app.route('/create-app', methods=['POST'])
def create_app():
    data = request.json
    new_app = UserApp(
        app_name=data['app_name'],
        app_dev_name=data['app_dev_name'],
        app_web_link=data.get('app_web_link'),
        app_app_link=data.get('app_app_link'),
        app_logo=data.get('app_logo'),
        app_created_on=data['app_created_on'],
        app_created_by=data['app_created_by']
    )
    db.session.add(new_app)
    db.session.commit()
    return create_response(201, "New app created successfully", new_app.to_dict())

@app.route('/apps/<int:id>', methods=['GET'])
def get_app(id):
    app = UserApp.query.get_or_404(id)
    return create_response(200, "App retrieved successfully", app.to_dict())

@app.route('/apps/<int:id>', methods=['PUT'])
def update_app(id):
    data = request.json
    app = UserApp.query.get_or_404(id)
    app.app_name = data['app_name']
    app.app_dev_name = data['app_dev_name']
    app.app_web_link = data.get('app_web_link')
    app.app_app_link = data.get('app_app_link')
    app.app_logo = data.get('app_logo')
    app.app_created_on = data['app_created_on']
    app.app_created_by = data['app_created_by']
    db.session.commit()
    return create_response(200, "App updated successfully", app.to_dict())

@app.route('/apps/<int:id>', methods=['DELETE'])
def delete_app(id):
    app = UserApp.query.get_or_404(id)
    db.session.delete(app)
    db.session.commit()
    return create_response(204, "App deleted successfully")

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
