from flask_sqlalchemy import SQLAlchemy

DB_NAME = "apartemen_db"
DB_USER = "root"
DB_PASSWORD = ""
DB_HOST = "localhost"

DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
db = SQLAlchemy()
