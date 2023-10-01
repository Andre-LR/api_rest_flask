from app.database import db
from app.models.Campaing import Campaing

from app.decorators import save_csv


class TeamRepository:

	@staticmethod
	def get(team_id: int):
		for campain in db.campains:
			if campain.id == team_id:
				return campain
		return None

	@staticmethod
	@save_csv
	def create(payload: dict):
		last_id = db.campains[-1].id
		campain = Campaing(id=last_id+1, **payload)
		db.campains.append(campain)
		return campain

	@staticmethod
	@save_csv
	def update(team_id: int, payload: dict):
		campaing = TeamRepository.get(team_id)
		if campaing is not None:
			for key, value in payload.items():
				setattr(campaing, key, value)
			return campaing
		return None

	@staticmethod
	@save_csv
	def delete(team_id: int):
		campaing = TeamRepository.get(team_id)
		db.campains.remove(campaing)
		return campaing
