from flask import Blueprint, render_template

paeds_protocol_bp = Blueprint('paeds_protocol', __name__, url_prefix='/paeds_protocol', template_folder='templates', static_folder='static')

@paeds_protocol_bp.route('/')
def index():

    return render_template('index.html')

@paeds_protocol_bp.route('/ios')
def ios():

    return render_template('index_ios.html')
