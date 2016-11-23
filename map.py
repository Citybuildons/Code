class Map:
	"""docstring for map :
	On fait des maps ! \o/ """
	def __init__(self, heigth, width):
		self.heigth = heigth
		self.width = width
		self.caselist = caselist[heigth,width] # creer la classe Case
		self.nhab = 0
		self.index = super.netage + 1 # index = numero de l'etage / netage = nombre d'etage 
		super.netage++
		self.connexion = []


	def modifynhab(diffnhab):
		# A mettre dans Maison
		self.nhab += diffnhab
		super.nhabVille = super.nhabVille + diffnhab


	# heigth.getter
	# def heigth():
	# 	return self.heigth

	# width.getter
	# def width():
	# 	return self.width



		


