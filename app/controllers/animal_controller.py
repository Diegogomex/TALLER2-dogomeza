from flask import Blueprint, jsonify, render_template
from app.models.animales import Gato, Perro, Huron, BoaConstrictor

animal_blueprint = Blueprint("animal", __name__)

gatos = [Gato("Kitty"), Gato("Snowball")]
perros = [Perro("Pluto"), Perro("Rex")]
hurones = [Huron("Paco"), Huron("Manolo")]
boas = [BoaConstrictor("Sonia"), BoaConstrictor("Ramona")]

@animal_blueprint.route("/", methods=["GET"])
def home():
    return render_template("sonidos.html")

@animal_blueprint.route("/animales/gatos/sonido", methods=["GET"])
def sonido_gatos():
    return jsonify([{"nombre": gato.nombre, "sonido": gato.hacer_sonido()} for gato in gatos])

@animal_blueprint.route("/animales/perros/sonido", methods=["GET"])
def sonido_perros():
    return jsonify([{"nombre": perro.nombre, "sonido": perro.hacer_sonido()} for perro in perros])

@animal_blueprint.route("/animales/hurones/sonido", methods=["GET"])
def sonido_hurones():
    return jsonify([{"nombre": huron.nombre, "sonido": huron.hacer_sonido()} for huron in hurones])

@animal_blueprint.route("/animales/boas/sonido", methods=["GET"])
def sonido_boas():
    return jsonify([{"nombre": boa.nombre, "sonido": boa.hacer_sonido()} for boa in boas])

@animal_blueprint.route("/animales/sonidos", methods=["GET"])
def sonidos_animales():
    return render_template("sonidos.html")
