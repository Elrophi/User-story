import os

class Config:
    """
    General configurations parent class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')   
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://el:maigoge@localhost/userstory' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'     

class ProdConfig(Config):
    """
    Production configuration child class
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")  
    pass 

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://el:maigoge@localhost/userstory' 
    pass
    

class DevConfig(Config):
    """
    Development config child class
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://el:maigoge@localhost/userstory' 

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}