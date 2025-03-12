from flask import Flask
from app.controllers.animal_controller import animal_blueprint


def create_app():
    app = Flask(__name__, template_folder="views")

    app.register_blueprint(animal_blueprint)

    return app

