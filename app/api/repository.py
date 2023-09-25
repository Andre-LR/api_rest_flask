import csv

db = []

with open('database.csv', 'r') as file:
	...


class TeamRepository:

	@staticmethod
	def get(team_id: int):
		...

	@staticmethod
	def create(payload: dict):
		...

	@staticmethod
	def update(team_id: int, payload: dict):
		...

	@staticmethod
	def delete(team_id: int):
		...
