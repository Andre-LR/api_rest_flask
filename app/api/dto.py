from flask_restx import Namespace, fields


namespace = Namespace(name='Team', description='Operations related to Teams.')

team_create_model = namespace.model(
	'team_create_model',
	{
		'year': fields.Integer(),
		'position': fields.Integer(),
		'name': fields.String(),
		'wins': fields.Integer(),
		'defeats': fields.Integer(),
		'draws': fields.Integer(),
		'goals_for': fields.Integer(),
		'goals_against': fields.Integer(),
		'goals_difference': fields.Integer(),
		'players_quantity': fields.Integer(),
		'age_average': fields.Float(),
		'foreigners': fields.Integer(),
		'total_value': fields.Integer(),
		'average_value': fields.Integer()
	}
)

team_update_model = namespace.model(
	'team_update_model',
	{
		'year': fields.Integer(),
		'position': fields.Integer(),
		'name': fields.String(),
		'wins': fields.Integer(),
		'defeats': fields.Integer(),
		'draws': fields.Integer(),
		'goals_for': fields.Integer(),
		'goals_against': fields.Integer(),
		'goals_difference': fields.Integer(),
		'players_quantity': fields.Integer(),
		'age_average': fields.Float(),
		'foreigners': fields.Integer(),
		'total_value': fields.Integer(),
		'average_value': fields.Integer()
	}
)


team_model = namespace.model(
	'team_model',
	{
		'id': fields.Integer(),
		'year': fields.Integer(),
		'position': fields.Integer(),
		'name': fields.String(),
		'wins': fields.Integer(),
		'defeats': fields.Integer(),
		'draws': fields.Integer(),
		'goals_for': fields.Integer(),
		'goals_against': fields.Integer(),
		'goals_difference': fields.Integer(),
		'players_quantity': fields.Integer(),
		'age_average': fields.Float(),
		'foreigners': fields.Integer(),
		'total_value': fields.Integer(),
		'average_value': fields.Integer()
	}
)
