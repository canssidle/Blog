import os

class Config:
    ULOADED_PHOTOS_DEST="app/static/photos"
    configure_uploads(app,(photos, media))

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("MAIL_USERNAME")
    
class DevConfig(Config):
    DEBUG = True

config_options ={"production":ProdConfig,"default":DevConfig}

