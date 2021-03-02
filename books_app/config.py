"""Initialize Config class to access environment variables."""
from dotenv import load_dotenv
import os

load_dotenv()

class Config(object):
    """Set environment variables."""

    DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
