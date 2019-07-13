import os
from msweb import app
dev_db = 'sqlite'
SECRET_KEY = os.getenvb('SECRET_KEY', 'MYDEV09 @ String')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')

