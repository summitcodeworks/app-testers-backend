from flask import Flask
from flask_cors import CORS  # Import CORS from flask_cors
from app.extensions import db, migrate  # cors will be initialized below
from app.models import user, user_app
from app.routes import user_routes, app_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    app.debug = True

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Initialize CORS with custom configuration
    CORS(app, resources={
        r"/*": {  # Apply to all routes
            "origins": "*",  # Adjust this to specific origins as needed
            "allow_headers": ["user_key"],  # Allow custom header
            "expose_headers": ["user_key"],  # Optional: if you want to expose the custom header
        }
    })

    # Register Blueprints (routes)
    app.register_blueprint(user_routes.bp)  # Register the user routes blueprint
    app.register_blueprint(app_routes.bp)    # Register the app routes blueprint

    return app
