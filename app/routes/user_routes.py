from flask import Blueprint, request
from app.models.user import User
from app.extensions import db
from app.utils.helper import create_response, user_key_required
from datetime import datetime

# Create a Blueprint instance
bp = Blueprint('user_routes', __name__)

@bp.route('/register-user', methods=['POST'])
def register_user():
    data = request.json

    existing_user = User.query.filter(
        (User.user_email == data['user_email']) | (User.user_key == data['user_key'])
    ).first()

    if existing_user:
        return create_response(409, "User already exists", existing_user.to_dict())  # 409 Conflict

    # If user does not exist, proceed to create a new user
    new_user = User(
        user_key=data['user_key'],
        user_name=data['user_name'],
        user_email=data['user_email'],
        user_creation_date=datetime.utcnow(),  # Set creation date to now
        use_flag=data.get('use_flag', True)  # Default to True if not provided
    )

    db.session.add(new_user)
    db.session.commit()

    return create_response(201, "New user created successfully", new_user.to_dict())


@bp.route('/users', methods=['GET'])
@user_key_required
def get_users():
    users = User.query.all()
    return create_response(200, "User list retrieved successfully", [user.to_dict() for user in users])

@bp.route('/users/<int:id>', methods=['GET'])
@user_key_required
def get_user(id):
    user = User.query.get_or_404(id)
    return create_response(200, "User retrieved successfully", user.to_dict())

@bp.route('/users/<int:id>', methods=['PUT'])
@user_key_required
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

@bp.route('/users/<int:id>', methods=['DELETE'])
@user_key_required
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return create_response(204, "User deleted successfully")