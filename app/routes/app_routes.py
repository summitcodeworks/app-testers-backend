from flask import Blueprint, request
from app.models.user_app import UserApp
from app.extensions import db
from app.utils.helper import create_response
from app.utils.helper import extract_package_name

bp = Blueprint('app_routes', __name__)

@bp.route('/app-lists', methods=['GET'])
def get_apps():
    apps = UserApp.query.all()
    return create_response(200, "App list retrieved successfully", [app.to_dict() for app in apps])


@bp.route('/create-app', methods=['POST'])
def create_app():
    data = request.json
    app_pkg_nme = extract_package_name(data.get('app_app_link'))

    if not app_pkg_nme:
        return create_response(400, "Invalid app link or package name could not be extracted", None)

    app_pkg_nme = app_pkg_nme.strip()

    existing_app = UserApp.query.filter(UserApp.app_pkg_nme.ilike(app_pkg_nme)).first()
    if existing_app:
        return create_response(400, "App with this package name already exists", None)

    new_app = UserApp(
        app_name=data['app_name'],
        app_dev_name=data['app_dev_name'],
        app_web_link=data.get('app_web_link'),
        app_app_link=data.get('app_app_link'),
        app_logo=data.get('app_logo'),
        app_created_on=data['app_created_on'],
        app_created_by=data['app_created_by'],
        app_pkg_nme=app_pkg_nme,
        use_flag=data.get('use_flag', True),
        app_desc=data.get('app_desc'),  # New field
        app_credit=data.get('app_credit')  # New field
    )

    db.session.add(new_app)
    db.session.commit()

    return create_response(201, "New app created successfully", new_app.to_dict())


@bp.route('/app-detail/<int:id>', methods=['GET'])
def get_app(id):
    # Query the database for the app using the provided app ID
    app = UserApp.query.get(id)

    # If no app is found, return a 404 error
    if app is None:
        return create_response(404, "App not found", None)

    return create_response(200, "App retrieved successfully", app.to_dict())



@bp.route('/apps/<int:id>', methods=['PUT'])
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
    app.use_flag = data.get('use_flag', app.use_flag)  # Update use_flag if provided
    app.app_desc = data.get('app_desc', app.app_desc)  # Update app_desc if provided
    app.app_credit = data.get('app_credit', app.app_credit)  # Update app_credit if provided

    db.session.commit()
    return create_response(200, "App updated successfully", app.to_dict())

@bp.route('/apps/<int:id>', methods=['DELETE'])
def delete_app(id):
    app = UserApp.query.get_or_404(id)
    db.session.delete(app)
    db.session.commit()
    return create_response(204, "App deleted successfully")
