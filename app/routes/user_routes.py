from flask import Blueprint, app, request
from app.models.user import User
from app.extensions import db
from app.utils.helper import create_response

bp = Blueprint('user_routes', __name__)

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


