from functools import wraps
from app.database import db

def save_csv(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		res = func(*args, **kwargs)
		db.save_csv()
		return res
	return wrapper
