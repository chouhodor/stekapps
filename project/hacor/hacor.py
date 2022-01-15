from flask import Blueprint, render_template , url_for

hacor_bp = Blueprint('hacor', __name__, url_prefix='/hacor', template_folder='templates', static_folder='static')

@hacor_bp.route('/')
def index():
    return render_template('hacor.html')