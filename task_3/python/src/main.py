import json
import os

from flask import Flask, jsonify, send_from_directory, request
from controller import Controller
from postgre import DbConnector

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({'name': 'alice', 'email': 'alice@outlook.com'})


@app.route('/gerb')
def gerb():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'mirea_gerb.png', mimetype='image/png'
    )


@app.route('/fruits', methods=['POST'])
def create_fruit():
    data = json.loads(request.data)
    response = controller.create_fruit(data)
    return jsonify(response)


@app.route('/fruits', methods=['GET'])
def get_fruits():
    response = controller.get_fruits()
    return jsonify(response)


if __name__ == '__main__':
    postgre_port = os.getenv('PSQL_PORT')
    db_connector = DbConnector(
        dbname='fruits', user='postgres',
        password='123456', host=f'db', port=5432,
    )
    controller = Controller(db_connector)
    app.run(debug=True, host='0.0.0.0', port=5000)
