import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://debarunlahiri:password@localhost/app_testers'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
