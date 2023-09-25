from dataclasses import dataclass


@dataclass
class Campaing:
	id: int
	year: int
	position: int
	name: str
	wins: int
	defeats: int
	draws: int
	goals_for: int
	goals_against: int
	goals_difference: int
	players_quantity: int
	age_average: float
	foreigners: int
	total_value: int
	average_value: int
	