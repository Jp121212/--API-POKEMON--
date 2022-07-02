from datetime import date, datetime
import datetime
from email.policy import default
from http import server
import json
from pydoc import doc
import select
from sqlite3 import Date, DateFromTicks, Time
from time import time
from venv import create
from sqlalchemy import DateTime
from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash,generate_password_hash
from flask_restful import Resource,Api
from sqlalchemy.sql import func 
from flask_cors import CORS


app = Flask(__name__)
CORS(app,resources={r"/api/*": {"origins":"*"}},)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/pokemon'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)

auth = Blueprint("auth", __name__, url_prefix="/api")



class Pokemones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    tipo = db.Column(db.String(80), nullable=False)
    edad = db.Column(db.Integer,nullable=False)
    movimientos = db.Column(db.String(90),nullable=False)
    imagenPerfil = db.Column(db.String(255),nullable=False)
    imagenadc = db.Column(db.String(255),nullable= False)
    peso = db.Column(db.String(5),nullable=False)
    descripcion = db.Column(db.String(400),nullable=False)

    
        
def __repr__(self):
        return '<Usuario %r>' % self.nombre

db.create_all()



class IndexRoute(Resource):
    def get(self):
        return {'response': 'Hola, Bienvenido A mi PokedexAPI :)'}

class IndexUsuario(Resource):
    def get(self):
        pokemones = Pokemones.query.all()
        response = []
        if pokemones:
            for pokemon in pokemones:
                response.append({
                "id": pokemon.id,
                "nombre": pokemon.nombre,
                "tipo": pokemon.tipo,
                "imagenPerfil": pokemon.imagenPerfil
                })
        return {'response': response}, 200

    def post(self):
        pokemonacrear = request.get_json()
        pokemonacrear = request.get_json()
        if pokemonacrear is None:
            return "Los campos estan vacios", 400
        if 'nombre' not in pokemonacrear:
            return 'Especificar nombre es obligatorio',400
        if 'tipo' not in pokemonacrear:
            return 'Especificar el tipo es obligatorio',400
        if 'edad' not in pokemonacrear:
            return 'Especificar edad es obligatorio', 400 
        if 'movimientos' not in pokemonacrear:
            return "Al menos un movimiento es obligatorio",400
        if "imagenPerfil" not in pokemonacrear:
            return "Especificar imagen es obligatorio",400
        if "imagenadc" not in pokemonacrear:
            return "Especificar imagen adicional es obligatorio",400
        if "peso" not in pokemonacrear:
            return "Especificar Peso es obligatorio"
        if "descripcion" not in pokemonacrear:
            return "Especificar descripcion es obligatorio"
        else:
            pokemon = Pokemones(nombre=pokemonacrear['nombre'],edad=pokemonacrear['edad'], tipo=pokemonacrear['tipo'],movimientos=pokemonacrear['movimientos'],imagenPerfil=pokemonacrear['imagenPerfil'],imagenadc=pokemonacrear['imagenadc'],peso=pokemonacrear["peso"],descripcion=pokemonacrear["descripcion"])
            db.session.add(pokemon)
            db.session.commit()
            return { "response": "Pokemon registrado exitosamente!"}, 201




auth
class PokemonApi(Resource):
 def get(self):
        pokemones = Pokemones.query.all()
        response = []
        if pokemones:
            for pokemon in pokemones:
                response.append({
                "id": pokemon.id,
                "nombre": pokemon.nombre,
                "tipo": pokemon.tipo,
                "edad": pokemon.edad,
                "movimientos": pokemon.movimientos,
                "imagenPerfil": pokemon.imagenPerfil,
                "imagenadc" : pokemon.imagenadc,
                "peso": pokemon.peso,
                "descripcion": pokemon.descripcion
                })
        return {'response': response}, 200







class PokemonbyID(Resource):
    def get(self, id):
        pokemon = Pokemones.query.filter_by(id=id).first()
        if pokemon == None:
            return ({"Malas noticias": "No se encuentran Pokemones registrados  con el id:  "+ str (id) }),200
        else:
            return {'Pokemon': {
                "id": pokemon.id,
                "nombre": pokemon.nombre,
                "tipo": pokemon.tipo,
                "edad": pokemon.edad,
                "movimientos": pokemon.movimientos,
                "imagenPerfil": pokemon.imagenPerfil,
                "imagenadc": pokemon.imagenadc,
                "peso": pokemon.peso,
                "descripcion": pokemon.descripcion
               
        }}, 200

    def put(self, id):
        pokemon = Pokemones.query.filter_by(id=id).first()
        datos = request.get_json()
        # TODO: LOOKUP 'ARGUMENT PARSING for Flask-RESTful'
        pokemon.nombre = datos['nombre']
        pokemon.edad = datos['edad']
        pokemon.tipo = datos['tipo']
        pokemon.movimientos = datos['movimientos']
        pokemon.imagenPerfil =  datos['imagenPerfil']
        pokemon.imagenadc = datos['imagenadc']
        pokemon.peso = datos['peso']
        pokemon.descripcion = datos['descripcion']        
        db.session.commit()
        return {"response": "Pokemon actualizado con exito!"}

    def delete(self, id):
        pokemon = Pokemones.query.filter_by(id=id).first()
        db.session.delete(pokemon)
        db.session.commit()
        return { "response": "Usuario con id: {pokemon}. Borrado exitosamente. ".format(pokemon=id)}, 203




# *Routes
# GET
api.add_resource(IndexRoute, '/')
# GET, POST
api.add_resource(IndexUsuario, '/pokemones')
# GET, PUT, DELETE
api.add_resource(PokemonbyID, '/pokemones/<int:id>')
#GET API
api.add_resource(PokemonApi, '/api/pokemonapi')


db.session.commit()