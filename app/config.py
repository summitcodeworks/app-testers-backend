import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://debarunlahiri:password@localhost/app_testers')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
