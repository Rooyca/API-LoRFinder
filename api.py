from flask import Flask
from flask_restful import Api, Resource, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Players.db'
db = SQLAlchemy(app)

class Players(db.Model):
	__tablename__ = "players"
	id = db.Column(db.Integer, primary_key=True)
	region = db.Column(db.String, nullable=False)
	name = db.Column(db.String, nullable=False)
	puuid = db.Column(db.String, nullable=False)


resource_fields = {
    'id':fields.Integer,
    'region':fields.String,
    'name':fields.String,
    'puuid':fields.String
}

class Player(Resource):
    @marshal_with(resource_fields)
    def get(self, name):
        result = Players.query.filter_by(name=name).first()
        return result

api.add_resource(Player, "/v1/<string:name>")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=6767)