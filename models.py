from app import db

class User(db.Model):
    __tablename__ = 'users'  # Table name in the database

    user_id = db.Column(db.Integer, primary_key=True)  # Primary key
    user_key = db.Column(db.String, nullable=False)      # User key
    user_name = db.Column(db.String, nullable=False)     # User name
    user_email = db.Column(db.String, nullable=False, unique=True)  # User email, must be unique
    user_creation_date = db.Column(db.Date, nullable=False)  # Date the user was created
    use_flag = db.Column(db.Boolean, default=True)       # Active status of the user

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