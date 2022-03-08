from flask import Blueprint, render_template , url_for, request, redirect
from ..models import Snakes, Snake_location


snake_data_bp = Blueprint('snake_data', __name__, url_prefix='/snake-data', template_folder='templates', static_folder='static')

@snake_data_bp.route('/')
def index():

    snake_list = []

    return render_template('snake_index.html')

@snake_data_bp.route('/get_snake_list', methods=['POST'])
def get_snake_list():

    region = request.form['region']

    snake_list = Snake_location.query.filter_by(location=region).all()

    return redirect(url_for('index'),
    snake_list=snake_list
    )


@snake_data_bp.route('/test')
def test():

    #Job.query.filter(Job.id.notin_([j.id for j in person.jobs]))

    snake_list = Snake_location.query.filter_by(state='pahang').all()

    #snake_data = Snake_location.query.filter(Snake_location.id.in_(snake_id.locations))

    data_list = []

    for s in snake_list:
        data_list.append(s.snake_id)

    snake_data = [Snakes.query.get(i) for i in data_list]

    snake_names = [a.name_en for a in snake_data]

    print(snake_names)




    return render_template('snake_index.html')