from flask import Blueprint, render_template , url_for

landing_bp = Blueprint('landing', __name__, url_prefix='/', template_folder='templates', static_folder='static')

@landing_bp.route('/')
def index():
    return render_template('landing.html')