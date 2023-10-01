import json
import requests

URL = 'http://localhost:5000/teams'

headers = {
	'Content-type':'application/json', 
	'Accept':'application/json'
}

def consulta():
	res = requests.get(f'{URL}/12')
	print(res)

def insercao():
	data = {
		'year': 2021,
		'position': 20,
		'name': 'BBBrêmio',
		'wins': 0,
		'defeats': 38,
		'draws': 0,
		'goals_for': 0,
		'goals_against': 68,
		'goals_difference': 68,
		'players_quantity': 29,
		'age_average': 29.5,
		'foreigners': 3,
		'total_value': 4892243,
		'average_value': 834588,
	}
	res = requests.post(f'{URL}', data=json.dumps(data), headers=headers)
	print(res)

def atualizacao():
	data = {
		'position': 1
	}
	res = requests.put(f'{URL}/12', data=json.dumps(data), headers=headers)
	print(res)

def delecao():
	res = requests.delete(f'{URL}/123')
	print(res)

consulta()
insercao()
atualizacao()
delecao()
