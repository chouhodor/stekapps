from flask import Blueprint, render_template , url_for

dengue_bp = Blueprint('dengue', __name__, url_prefix='/dengue', template_folder='templates', static_folder='static')

@dengue_bp.route('/')
def index():
    return render_template('dengue.html')