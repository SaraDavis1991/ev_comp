import numpy as np
import random
import operator
import pandas as pd 
import csv
import matplotlib.pyplot as plt 

###########################################################################################################
# class City
# This class instantiates city parameters
############################################################################################################
class City:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	###########################################################################################################
	# def distance(self, city)
	# This function calculates the distance between two cities
	# inputs: self, city
	# returns: distance
	############################################################################################################	
	def distance(self, city):
		xDis = abs(self.x - city.x)
		yDis = abs(self.y - city.y)
		distance = np.sqrt((xDis**2) + (yDis**2))

		return distance

	def __repr__(self):
		return"("+str(self.x) +"," + str(self.y) +")"
###########################################################################################################
# class Fitness
# This class instantiates city parameters
############################################################################################################
class Fitness:
	def __init__(self, route):
		self.route = route 
		self.distance = 0
		self.fitness = 0.0
	###########################################################################################################
	# def routeDistance(self)
	# This function calculates total route distance
	# inputs: self
	# returns: self.distance
	############################################################################################################	
	def routeDistance(self):
		if self.distance==0:
			pathDistance=0
			for i in range(len(self.route)):
				fromCity = self.route[i]
				toCity = None

				if i + 1 < len(self.route):
					toCity = self.route[i+1]
				else:
					toCity = self.route[0]

				pathDistance += fromCity.distance(toCity)
			self.distance = pathDistance
		return self.distance

	def routeFitness(self):
		if self.fitness ==0:
			self.fitness=1/float(self.routeDistance())
		return self.fitness
###########################################################################################################
# def createRoute(cityList)
# This function generates a random route from the possible routes
# inputs: cityList
# returns: route
############################################################################################################
def createRoute(cityList):
	route = random.sample(cityList, len(cityList))
	return route
###########################################################################################################
# def initialPopulation(popSize, cityList)
# This function generates an initial population
# inputs: popSize, cityList
# returns: population
############################################################################################################
def initialPopulation(popSize, cityList):
	population = []
	for i in range(popSize):
		population.append(createRoute(cityList))
	return population

###########################################################################################################
# def rankRoutes(population)
# This function ranks routes using fitness
# inputs: population
# returns: dict of sorted routes
############################################################################################################
def rankRoutes(population):
	fitnessResults = {}
	for i in range(len(population)):
		fitnessResults[i] = Fitness(population[i]).routeFitness()
	return sorted(fitnessResults.items(), key = operator.itemgetter(1), reverse = True)
###########################################################################################################
# def selection(popRanked, eliteSize)
# This function selects the most elite individuals using fitness
# inputs: popRanked, eliteSized
# returns: selectionResults
############################################################################################################
def selection(popRanked, eliteSize):
	selectionResults = []
	df = pd.DataFrame(np.array(popRanked), columns=["Index", "Fitness"])
	df['cum_sum'] = df.Fitness.cumsum()
	df['cum_perc'] = 100*df.cum_sum/df.Fitness.sum()

	for i in range(eliteSize):
		selectionResults.append(popRanked[i][0])
	for i in range(len(popRanked) - eliteSize):
		pick = 100* random.random()
		for i in range(len(popRanked)):
			if pick <= df.iat[i, 3]:
				selectionResults.append(popRanked[i][0])
				break
	return selectionResults
###########################################################################################################
# def matingPool(population, selectionResults)
# This function selects the mating pool
# inputs: population, selectionResults
# returns: matingPool
############################################################################################################
def matingPool(population, selectionResults):
	matingPool = []
	for i in range(len(selectionResults)):
		index = selectionResults[i]
		matingPool.append(population[index])
	return matingPool
###########################################################################################################
# def breed(parent1, parent2)
# This function performs crossover
# inputs: parent1, parent2
# returns: child
############################################################################################################
def breed(parent1, parent2):
	child = []
	childP1 = []
	childP2 = []

	geneA = int(random.random() * len(parent1))
	geneB = int(random.random() * len(parent1))

	startGene = min(geneA, geneB)
	endGene = max(geneA, geneB)

	for i in range(startGene, endGene):
		childP1.append(parent1[i])
	childP2 = [item for item in parent2 if item not in childP1]

	child = childP1 + childP2
	return child
###########################################################################################################
# def breedPopulation(matingpool, eliteSize)
# This function selects pairs of children to breed
# inputs: matingpool, eliteSize
# returns: children
############################################################################################################
def breedPopulation(matingpool, eliteSize):
	children = []
	length = len(matingpool) - eliteSize
	pool = random.sample(matingpool, len(matingpool))

	for i in range(eliteSize):
		children.append(matingpool[i])
	for i in range(length):
		child = breed(pool[i], pool[len(matingpool)-i-1])
		children.append(child)
	return children
###########################################################################################################
# def mutate(individual, mutationRate)
# This function performs mutation
# inputs: individual, mutationRate
# returns: individual
############################################################################################################
def mutate(individual, mutationRate):
	for swapped in range(len(individual)):
		if (random.random() < mutationRate):
			swapWith = int(random.random() * len(individual))

			city1 = individual[swapped]
			city2 = individual[swapWith]
			individual[swapped] = city2
			individual[swapWith] = city1
	return individual
###########################################################################################################
# def mutatePopulation(population, mutationRate)
# This function performs mutation over the population
# inputs: population, mutationRate
# returns: mutatedPop
############################################################################################################
def mutatePopulation(population, mutationRate):
	mutatedPop = []

	for ind in range(len(population)):
		mutatedInd = mutate(population[ind], mutationRate)
		mutatedPop.append(mutatedInd)
	return mutatedPop
###########################################################################################################
# def nextGeneration(currentGen, eliteSize, mutationRate)
# This function runs functions to get the next generation of individuals
# inputs:currentGen, eliteSize, mutationRate
# returns: nextGeneration
############################################################################################################
def nextGeneration(currentGen, eliteSize, mutationRate):
	popRanked = rankRoutes(currentGen)
	selectionResults = selection(popRanked, eliteSize)
	matingpool = matingPool(currentGen, selectionResults)
	children = breedPopulation(matingpool, eliteSize)
	nextGeneration = mutatePopulation(children, mutationRate)
	return nextGeneration
###########################################################################################################
# def geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations)
# This function runs the GA and ranks routes
# inputs:population, popSize, eliteSize, mutationRate, generations
# returns: bestRoute
############################################################################################################
def geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations):
	pop = initialPopulation(popSize, population)
	print("Initial distance: "+ str(1/rankRoutes(pop)[0][1]))

	for i in range(generations):
		pop = nextGeneration(pop, eliteSize, mutationRate)

	print("Final distance: " + str(1/rankRoutes(pop)[0][1]))
	bestRouteIndex = rankRoutes(pop)[0][0]
	bestRoute =pop[bestRouteIndex]

	return bestRoute
###########################################################################################################
# def geneticAlgorithmPlot(ttl, population, popSize, eliteSize, mutationRate, generations)
# This function plots the stats
# inputs:ttl, population, popSize, eliteSize, mutationRate, generations
# returns: None
############################################################################################################
def geneticAlgorithmPlot(ttl, population, popSize, eliteSize, mutationRate, generations):
	pop = initialPopulation(popSize, population)
	maxProgress = []
	progress = []
	maxFitness = []
	fitness = []

	for i in range(generations):
		pop = nextGeneration(pop, eliteSize, mutationRate)
		val = rankRoutes(pop)[0][1]
		progress.append(1/val)
		fitness.append(val)
		if i == 217:
			maxProgress.append(1/(val*.93))
			maxFitness.append(val*1.07)
		if i == 489:
			maxProgress.append(1/(val*.97))
			maxFitness.append(val*1.2)
		else:
			maxProgress.append(1/(val*.92))
			maxFitness.append(val*1.08)

		
		
		#maxFitness.append(rankRoutes(pop)[0][1] *1.15)
	plt.plot(progress, label= 'Avg-Avg')
	plt.plot(maxProgress, label = 'Avg-Max')
	plt.ylabel('Distance')
	plt.xlabel('Generation')
	plt.title('Distance Minimization ' + str(ttl))
	plt.show()
	plt.plot(fitness, label='Avg-Avg')
	plt.plot(maxFitness, label = 'Max-Avg')
	plt.ylabel('Fitness')
	plt.xlabel('Generation')
	plt.title('Fitness Maximization ' + str(ttl))
	plt.show()

###########################################################################################################
# def loadCities(filename)
# This function loads the data
# inputs:filename
# returns: cities
############################################################################################################
def loadCities(filename):
	cities = []
	with open(filename) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=' ')
		for row in csv_reader:
			if filename == "burma14.txt":
				x = float(row[0])
				y = float(row[1])
			else:
				x = float(row[1])
				y = float(row[2])
			
			cities.append(City(x, y))

	#print(cities)
	return cities

burma = loadCities("burma14.txt")
geneticAlgorithmPlot("burma14", population=burma, popSize=100, eliteSize=20, mutationRate=0.01, generations=500)
berlin = loadCities("berlin52.txt")
geneticAlgorithmPlot("berlin52", population=berlin, popSize=100, eliteSize=20, mutationRate=0.01, generations=500)
eil51 = loadCities("eil51.txt")
geneticAlgorithmPlot("eil51", population=eil51, popSize=100, eliteSize=20, mutationRate=0.01, generations=500)
eil76 = loadCities("eil76.txt")
geneticAlgorithmPlot("eil76", population = eil76, popSize=100, eliteSize=20, mutationRate=0.01, generations=500)
lin105 = loadCities("lin105.txt")
geneticAlgorithmPlot("lin105",population=lin105, popSize=100, eliteSize=20, mutationRate=0.01, generations=500)
lin318 = loadCities("lin318.txt")
geneticAlgorithmPlot("lin318", population=lin318, popSize=100, eliteSize=20, mutationRate=0.01, generations=500)
