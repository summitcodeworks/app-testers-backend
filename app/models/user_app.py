from app.extensions import db

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
    app_pkg_nme = db.Column(db.String)  # Package name (new field)

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
            'app_pkg_nme': self.app_pkg_nme  # Include the package name in the dictionary
        }