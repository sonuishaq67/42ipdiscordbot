import re

def get_bleach(r: str):
	"""
	The get bleach function revibes a route r
	and returns one of their lines, this function has been created to 
	mainly work with the bleach.txt file.
	"""
	with open(r) as file:
		try:
			msg = random.choice(file.readlines())
			return re.search(r"\[([A-Za-z0-9_]+)\]", '{}'.format(msg))
		
		except:
			return 'Error in the get_bleach() function'
	
