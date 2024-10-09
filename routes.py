from flask import Blueprint, jsonify, request
from app import db
from models import Item

api_blueprint = Blueprint('api', __name__)

# Create a new item
@api_blueprint.route('/register-user', methods=['POST'])
def create_item():
    data = request.json
    new_item = Item(name=data['name'], description=data.get('description', ''))
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dict()), 201

# Read all items
@api_blueprint.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items])

# Read a single item by ID
@api_blueprint.route('/items/<int:id>', methods=['GET'])
def get_item(id):
    item = Item.query.get_or_404(id)
    return jsonify(item.to_dict())

# Update an item by ID
@api_blueprint.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    data = request.json
    item = Item.query.get_or_404(id)
    item.name = data['name']
    item.description = data.get('description', '')
    db.session.commit()
    return jsonify(item.to_dict())

# Delete an item by ID
@api_blueprint.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return '', 204


@api_blueprint.route('/test-db-conn', methods=['GET'])
def test_connection():
    try:
        # Attempt a simple query to test the connection
        result = db.session.execute('SELECT 1')
        return jsonify({'status': 'success', 'message': 'Database connection is working!'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
    
    
@api_blueprint.route('/register-user', methods=['POST'])
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
    return jsonify(new_user.to_dict()), 201
