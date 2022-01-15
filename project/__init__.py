from flask import Flask 

def create_app():
    app = Flask(__name__)

    from .dengue import dengue 
    from .hacor import hacor
    from .landing import landing
    from .paeds_protocol import paeds_protocol

    app.register_blueprint(dengue.dengue_bp)
    app.register_blueprint(hacor.hacor_bp)
    app.register_blueprint(landing.landing_bp)
    app.register_blueprint(paeds_protocol.paeds_protocol_bp)

    return app