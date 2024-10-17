from app.extensions import db

class UserApp(db.Model):
    __tablename__ = 'user_apps'

    app_id = db.Column(db.BigInteger, primary_key=True)  # Changed to BigInteger to match bigserial
    app_name = db.Column(db.String, nullable=False)
    app_dev_name = db.Column(db.String, nullable=False)
    app_web_link = db.Column(db.Text)
    app_app_link = db.Column(db.Text)
    app_logo = db.Column(db.Text)
    app_created_on = db.Column(db.Date, nullable=False)
    app_created_by = db.Column(db.Integer, nullable=False)
    app_pkg_nme = db.Column(db.Text)  # Changed to Text to match the database schema
    use_flag = db.Column(db.Boolean, default=True)  # Ensure the field is present with default
    app_desc = db.Column(db.Text)  # New field for app description
    app_credit = db.Column(db.Integer)  # New field for app credit

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
            'app_pkg_nme': self.app_pkg_nme,
            'use_flag': self.use_flag,  # Ensure this field is included in the dict
            'app_desc': self.app_desc,  # Include app_desc in the serialization
            'app_credit': self.app_credit  # Include app_credit in the serialization
        }
