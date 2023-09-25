from flask_restx import Namespace, fields


namespace = Namespace(name='Team', description='Operations related to Teams.')

team_create_model = namespace.model(
	'team_create_model',
	{
		'name': fields.String()
	}
)

team_update_model = namespace.model(
	'team_update_model',
	{
		'name': fields.String()
	}
)


team_model = namespace.model(
	'team_model',
	{
		'id': fields.Integer(),
		'name': fields.String()
	}
)
