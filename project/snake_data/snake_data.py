from flask import Blueprint, render_template , url_for
from ..models import Snakes, Snake_location


snake_data_bp = Blueprint('snake_data', __name__, url_prefix='/snake-data', template_folder='templates', static_folder='static')

@snake_data_bp.route('/')
def index():
    return render_template('snake_index.html')

@snake_data_bp.route('/test')
def test():

    snake_list = Snake_location.query.filter_by(snake_id=3).all()

    print(snake_list)

    return render_template('snake_index.html')