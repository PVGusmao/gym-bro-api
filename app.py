from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from flask_bcrypt import Bcrypt

from flask_restx import Api, Resource, fields

from flask_jwt_extended import jwt_required, JWTManager, get_jwt_identity

from controller.exercise import ExerciseController
from controller.user import UserController
from model.exercise import Exercises
from model.user import User

from swagger.api.instance import server
from swagger.models.auth import user
from swagger.models.register import register
from swagger.models.exercise import exercise_register

app, api = server.app, server.api

CORS(app)
bcrypt = Bcrypt(app)

app.config["JWT_SECRET_KEY"] = "my_secret_key"
jwt = JWTManager(app)

@api.route('/login')
class Auth(Resource):
    @api.doc(body=user)
    def post(self, ):
        email = request.json.get('email')
        password = request.json.get('password')

        user_controller = UserController()

        data = user_controller.login(email, password, bcrypt)

        return make_response(jsonify(data), data['status'])


@api.route('/register')
class Register(Resource):
    @api.doc(body=register)
    def post(self, ):
        user = User(
            first_name=request.json.get("first_name"),
            last_name=request.json.get("last_name"),
            cpf=request.json.get("cpf"),
            birth_date=request.json.get("birth_date"),
            email=request.json.get("email"),
            cep=request.json.get("cep"),
            address=request.json.get("address"),
            state=request.json.get("state"),
            city=request.json.get("city"),
            neighborhood=request.json.get("neighborhood"),
            number=request.json.get("number"),
            complement=request.json.get("complement"),
            password=bcrypt.generate_password_hash(
                request.json.get('password')).decode('utf-8')
        )

        user_controller = UserController()

        data = user_controller.register_user(user)

        return make_response(jsonify(data), data['status'])

@api.route('/me')
class Me(Resource):
    @jwt_required()
    @api.doc()
    def get(self, ):
        user = get_jwt_identity()

        return make_response(jsonify(user), 200)

@api.route('/exercise')
class Exercise(Resource):
    @jwt_required() 
    def get(self, ):
        user = get_jwt_identity()
        user_id = user["id"]

        exController = ExerciseController()

        data = exController.get_all_exercises(user_id)

        return make_response(jsonify(data), data['status'])

    @api.doc(body=exercise_register)
    @jwt_required()
    def post(self,):
        user = get_jwt_identity()

        day_serie = request.json.get("day_serie")
        identify = request.json.get("identify")
        exercises = request.json.get("exercise")

        new_data = 0

        for each in exercises:
            exercise = Exercises(
                day_serie=day_serie,
                name=each["name"],
                muscle_group=each["muscle_group"],
                video_exercise=None,
                series=each["series"],
                series_repeats=each["series_repeats"],
                identify=identify,
                user_id=user['id'],
            )

            exercise_controller = ExerciseController()

            new_data = exercise_controller.add_exercise(exercise)

            if new_data['status'] != 200:
                break

        return make_response(jsonify(new_data), new_data["status"])

@app.route('/exercise/remove/<exercise_id>', methods=['DELETE'])
@jwt_required()
def delete(exercise_id):
    exController = ExerciseController()

    data = exController.remove_exercise(exercise_id)

    return make_response(jsonify(data), data['status'])


@app.route('/exercise/lastserie', methods=['GET'])
@jwt_required()
def get_last_serie():
    user = get_jwt_identity()
    user_id = user["id"]

    exController = ExerciseController()

    data = exController.get_last_serie(user_id)

    return make_response(jsonify(data), data['status'])
