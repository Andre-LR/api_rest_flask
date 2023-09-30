import csv

from typing import List

from app.models.Campaing import Campaing


class Database:

	def __init__(self):
		self.campains : List[Campaing] = []
		self.load_db_from_csv()

	def save_csv(self):
		with open('database.csv', 'w') as file:
			writer = csv.writer(file)
			for campaing in self.campains:
				row = [
					campaing.year,
					campaing.position,
					campaing.name,
					campaing.wins,
					campaing.defeats,
					campaing.draws,
					f'{campaing.goals_for}:{campaing.goals_against}',
					campaing.goals_difference,
					campaing.players_quantity,
					campaing.age_average,
					campaing.foreigners,
					campaing.total_value,
					campaing.average_value
				]
				writer.writerow(row)

	def load_db_from_csv(self):
		with open('database.csv', 'r') as file:
			reader = csv.reader(file)
			data = list(reader)
		
		i = 0
		for d in data:
			campain = Campaing(
				id=i,
				year=d[0],
				position=d[1],
				name=d[2],
				wins=d[3],
				defeats=d[4],
				draws=d[5],
				goals_for=d[6].split(':')[0],
				goals_against=d[6].split(':')[1],
				goals_difference=d[7],
				players_quantity=d[8],
				age_average=float(d[9].replace(',', '.')),
				foreigners=d[10],
				total_value=d[11],
				average_value=d[12]
			)
			self.campains.append(campain)
			i+=1

db = Database()
