from flask import Flask
from app.extensions import db, migrate, cors
from app.models import user, user_app
from app.routes import user_routes, app_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    app.debug = True

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    # Register Blueprints (routes)
    from app.routes import user_routes, app_routes
    app.register_blueprint(user_routes.bp)  # Register the blueprint here
    app.register_blueprint(app_routes.bp)

    return app