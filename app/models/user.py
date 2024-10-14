from app.extensions import db

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    user_key = db.Column(db.String, nullable=False)
    user_name = db.Column(db.String, nullable=False)
    user_email = db.Column(db.String, nullable=False, unique=True)
    user_creation_date = db.Column(db.Date, nullable=False)
    use_flag = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'user_key': self.user_key,
            'user_name': self.user_name,
            'user_email': self.user_email,
            'user_creation_date': self.user_creation_date,
            'use_flag': self.use_flag,
        }
