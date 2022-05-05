from console import bcolors

class logger:
	@staticmethod
	def log(string,mtype='INFO',color=bcolors.ENDC):
		if color is 'green':
			color = bcolors.OKGREEN
		elif color is 'blue':
			color = bcolors.OKBLUE
		elif color is 'red':
			color = bcolors.FAIL
		print(color + mtype + '\t   ' + string + bcolors.ENDC)

