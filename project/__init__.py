from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'appsforthepeople'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from .dengue import dengue 
    from .snake_data import snake_data
    from .landing import landing
    from .paeds_protocol import paeds_protocol

    app.register_blueprint(dengue.dengue_bp)
    app.register_blueprint(snake_data.snake_data_bp)
    app.register_blueprint(landing.landing_bp)
    app.register_blueprint(paeds_protocol.paeds_protocol_bp)

    return app