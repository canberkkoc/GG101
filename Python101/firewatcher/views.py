from flask import Blueprint, render_template

from firewatcher.models import Cities, WildFires

root = Blueprint("", __name__)


@root.route("/")
def homepage():
    try:
        city_response = Cities.query.order_by("name").all()
        return render_template('index.html', cities=city_response)
    except Exception as e:
        return render_template('index.html', cities=[e])


@root.route("/cities/<city_id>/fires")
def fires(city_id):
    try:
        fire_response = WildFires.query.filter_by(city=city_id).all()
        city = Cities.query.filter_by(id=city_id).one()
        return render_template('fires.html', fires=fire_response, city=city)
    except Exception as e:
        return render_template('hata.html', error=e)
