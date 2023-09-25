from flask import Blueprint, request
from flask_restx import Resource

from app.api.service import TeamService

from .dto import namespace, team_create_model, team_model, team_update_model


@namespace.route('')
class TeamCreateControler(Resource):

	@namespace.expect(team_create_model)
	@namespace.marshal_with(team_model)
	def post(self):
		return TeamService.create(namespace.payload)


@namespace.route('/<int:team_id>')
class TeamControler(Resource):

	@namespace.marshal_with(team_model)
	def get(self, team_id: int):
		return TeamService.get(team_id)

	@namespace.expect(team_update_model)
	@namespace.marshal_with(team_model)
	def put(self, team_id: int):
		return TeamService.update(team_id, request.args)

	@namespace.marshal_with(team_model)
	def delete(self, team_id: int):
		return TeamService.delete(team_id)
