from .repository import TeamRepository


class TeamService:

	@staticmethod
	def get(team_id: int):
		return TeamRepository.get(team_id)

	@staticmethod
	def create(payload: dict):
		return TeamRepository.create(payload)

	@staticmethod
	def update(team_id: int, payload: dict):
		return TeamRepository.update(team_id, payload)

	@staticmethod
	def delete(team_id: int):
		return TeamRepository.delete(team_id)
