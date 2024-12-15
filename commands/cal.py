import calendar
from datetime import datetime

def run(args):
	try:
		if args:
			year, month = map(int, args.split())
			if month < 1 or month > 12:
				print('Month has to be between 1 and 12')
				return
		else:
			now = datetime.now()
			year, month = now.year, now.month
		print('\n', calendar.month(year, month))
	except ValueError:
		print("Invalid input. Please provide arguments in the format 'year month'.")
