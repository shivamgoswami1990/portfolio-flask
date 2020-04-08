import os
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['APP_SETTINGS'] = "config.ProductionConfig"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://ubuntu:postgres@localhost/portfolio"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Statistic


@app.route("/statistics")
def get_all():
    try:
        statistics = Statistic.query.all()
        return jsonify([e.serialize() for e in statistics])
    except Exception as e:
        return str(e)


@app.route("/statistic/<id_>")
def get_by_id(id_):
    try:
        statistic = Statistic.query.filter_by(id=id_).first()
        return jsonify(statistic.serialize())
    except Exception as e:
        return str(e)


@app.route("/submit_form", methods=['POST', 'OPTIONS'])
def submit_form():
    if request.method == 'OPTIONS':  # CORS preflight
        return _build_cors_prelight_response()
    elif request.method == 'POST':  # The actual request following the preflight
        name = request.get_json().get('name')
        email = request.get_json().get('email')
        subject = request.get_json().get('subject')
        message = request.get_json().get('message')
        try:
            statistic = Statistic(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            db.session.add(statistic)
            db.session.commit()
            return _corsify_actual_response(jsonify("Statistic added. statistic id={}".format(statistic.id)))
        except Exception as e:
            return str(e)


def _build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response


def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0:8000')
