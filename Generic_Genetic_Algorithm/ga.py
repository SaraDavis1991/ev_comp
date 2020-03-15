###################################################################################################################################################
# filename: ga.py
# author: Sara Davis 
# date: 10/1/2018
# version: 1.0
# description: Generic Genetic Algorithm
###################################################################################################################################################

import random
import numpy as np
import sys
from numpy.random import choice
import csv
np.set_printoptions(threshold=sys.maxsize)
import matplotlib.pyplot as plt

###########################################################################################################
# def generate_chromosome()
# Generate a 16 random 0's or 1's, return that as the chromosome
# inputs: X, K
# returns: centers (cluster centers)
############################################################################################################
def generate_chromosome():
	temp = []
	for i in range(16):
		val = random.randint(0, 1)
		#print(val)
		temp.append(val)
	return np.asarray(temp)
###########################################################################################################
# def generate_individual(num_chain)
# Chain together a series of chromosomes to form an individual
# inputs: num_chain
# returns: individual
############################################################################################################
def generate_individual(num_chain):
	temp = []
	for j in range (num_chain):
		temp.append(generate_chromosome())
	individual = np.asarray(temp).reshape(16*num_chain)

	return individual

###########################################################################################################
# def generate_population1()
# Generate an individual with 3 chained chromosomes, and form a population of 100
# inputs: None
# returns: population
############################################################################################################
def generate_population1():
	pop = []
	for i in range(100):
		ind= generate_individual(3)
		pop.append(ind)
	population=np.asarray(pop)

	return population

###########################################################################################################
# def generate_population1()
# Generate an individual with 2 chained chromosomes, and form a population of 100
# inputs: None
# returns: population
############################################################################################################
def generate_population2():
	pop = []
	for i in range(100):
		ind= generate_individual(2)
		pop.append(ind)
	population=np.asarray(pop)

	return population

###########################################################################################################
# def generate_population1()
# Generate an individual with 5 chained chromosomes, and form a population of 100
# inputs: None
# returns: population
############################################################################################################
def generate_population3():
	pop = []
	for i in range(100):
		ind= generate_individual(5)
		# print(len(ind))
		pop.append(ind)
	# print(pop)
	population=np.asarray(pop)

	return population

###########################################################################################################
# def generate_population1()
# Generate an individual with 30 chained chromosomes, and form a population of 100
# inputs: None
# returns: population
############################################################################################################
def generate_population4():
	pop = []
	for i in range(100):
		ind= generate_individual(30)
		pop.append(ind)
	population=np.asarray(pop)

	return population



###########################################################################################################
# def calculate_first_dejong(population)
# Use the first dejong funciton to evaluate the fitness of the chromosome
# inputs: population
# returns: sumall
############################################################################################################
def calculate_first_dejong(population):
	#print(population[:, :16])
	chrom1 = population[:, :16].dot(2**np.arange(population[:, :16].shape[1])[::-1])
	chrom2 = population[:, 17:32].dot(2**np.arange(population[:, 17:32].shape[1])[::-1])
	chrom3 = population[:, 33:].dot(2**np.arange(population[:, 33:].shape[1])[::-1])

	chrom1 = 5.12 * 2 / (2**16) * chrom1 -5.12
	chrom2 = 5.12 * 2 / (2**16) * chrom2 -5.12
	chrom3 = 5.12 * 2 / (2**16) * chrom3 -5.12

	sumAll = 81 - (chrom1 * chrom1 + chrom2* chrom2 + chrom3*chrom3) 

	return sumAll
###########################################################################################################
# def calculate_second_dejong(population)
# Use the second dejong funciton to evaluate the fitness of the chromosome
# inputs: population
# returns: val
############################################################################################################
def calculate_second_dejong(population):
	#print(population[:, :16])
	chrom1 = population[:, :16].dot(2**np.arange(population[:, :16].shape[1])[::-1])
	chrom2 = population[:, 17:32].dot(2**np.arange(population[:, 17:32].shape[1])[::-1])
	

	chrom1 = 2.048 * 2 / (2**16) * chrom1 - 2.048
	chrom2 = 2.048 * 2 / (2**16) * chrom2 - 2.048

	val =3906-( (100*(chrom1 **2- chrom2) **2) + (1-chrom1)**2)
 	#was 420
	return val
###########################################################################################################
# def calculate_third_dejong(population)
# Use the third dejong funciton to evaluate the fitness of the chromosome
# inputs: population
# returns: sumAll
############################################################################################################
def calculate_third_dejong(population):
	#print(population[:, :16])
	chrom1 = population[:, :16].dot(2**np.arange(population[:, :16].shape[1])[::-1])
	chrom2 = population[:, 16:32].dot(2**np.arange(population[:, 16:32].shape[1])[::-1])
	chrom3 = population[:, 32:48].dot(2**np.arange(population[:, 32:48].shape[1])[::-1])
	chrom4 = population[:, 48:64].dot(2**np.arange(population[:, 48:64].shape[1])[::-1])
	chrom5 = population[:, 64:].dot(2**np.arange(population[:, 64:].shape[1])[::-1])
	# print(population[:, 48:54])
	# print(population[:, 54:])
	#print(chrom4)
	# print(len(chrom5[0]))
	chrom1 = 5.12 * 2 / (2**16) * chrom1  - 5.12	
	chrom2 = 5.12 * 2 / (2**16) * chrom2  - 5.12
	chrom3 = 5.12 * 2 / (2**16) * chrom3  - 5.12
	chrom4 = 5.12 * 2 / (2**16) * chrom4  - 5.12
	chrom5 = 5.12 * 2 / (2**16) * chrom5  - 5.12  
	#print(chrom1)
	#print(chrom2)
	#print(chrom3)
	#print(chrom4)
	#print(chrom5)
	sumAll = 26 + (chrom1.astype(int) + chrom2.astype(int) + chrom3.astype(int) + chrom4.astype(int) + chrom5.astype(int))
	#print(sumAll)
	return sumAll.astype(float)
###########################################################################################################
# def calculate_fourth_dejong(population)
# Use the fourth dejong funciton to evaluate the fitness of the chromosome
# inputs: population
# returns: sumAll
############################################################################################################
def calculate_fourth_dejong(population):
	#NP.RANDOM.RANDN
	#print(len(population[0]))

	chrom1 = population[:, :16].dot(2**np.arange(population[:, :16].shape[1])[::-1])
	chrom2 = population[:, 17:32].dot(2**np.arange(population[:, 17:32].shape[1])[::-1])
	chrom3 = population[:, 33:48].dot(2**np.arange(population[:, 33:48].shape[1])[::-1])
	chrom4 = population[:, 49:54].dot(2**np.arange(population[:, 49:54].shape[1])[::-1])
	chrom5 = population[:, 55:70].dot(2**np.arange(population[:, 55:70].shape[1])[::-1])
	chrom6 = population[:, 71:86].dot(2**np.arange(population[:, 71:86].shape[1])[::-1])
	chrom7 = population[:, 87:102].dot(2**np.arange(population[:, 87:102].shape[1])[::-1])
	chrom8 = population[:, 103:118].dot(2**np.arange(population[:, 103:118].shape[1])[::-1])
	chrom9 = population[:, 119:134].dot(2**np.arange(population[:, 119:134].shape[1])[::-1])
	chrom10 = population[:, 135:150].dot(2**np.arange(population[:, 135:150].shape[1])[::-1])
	chrom11 = population[:, 151:166].dot(2**np.arange(population[:, 151:166].shape[1])[::-1])
	chrom12 = population[:, 167:182].dot(2**np.arange(population[:, 167:182].shape[1])[::-1])
	chrom13 = population[:, 183:198].dot(2**np.arange(population[:, 183:198].shape[1])[::-1])
	chrom14 = population[:, 199:214].dot(2**np.arange(population[:, 199:214].shape[1])[::-1])
	chrom15 = population[:, 215:231].dot(2**np.arange(population[:, 215:231].shape[1])[::-1])
	chrom16 = population[:, 232:247].dot(2**np.arange(population[:, 232:247].shape[1])[::-1])
	chrom17 = population[:, 248:263].dot(2**np.arange(population[:, 248:263].shape[1])[::-1])
	chrom18 = population[:, 264:279].dot(2**np.arange(population[:, 264:279].shape[1])[::-1])
	chrom19 = population[:, 280:295].dot(2**np.arange(population[:, 280:295].shape[1])[::-1])
	chrom20 = population[:, 296:311].dot(2**np.arange(population[:, 296:311].shape[1])[::-1])
	chrom21 = population[:, 312:327].dot(2**np.arange(population[:, 312:327].shape[1])[::-1])
	chrom22 = population[:, 328:343].dot(2**np.arange(population[:, 328:343].shape[1])[::-1])
	chrom23 = population[:, 344:359].dot(2**np.arange(population[:, 344:359].shape[1])[::-1])
	chrom24 = population[:, 360:375].dot(2**np.arange(population[:, 360:375].shape[1])[::-1])
	chrom25 = population[:, 376:391].dot(2**np.arange(population[:, 376:391].shape[1])[::-1])
	chrom26 = population[:, 392:407].dot(2**np.arange(population[:, 392:407].shape[1])[::-1])
	chrom27 = population[:, 408:423].dot(2**np.arange(population[:, 408:423].shape[1])[::-1])
	chrom28 = population[:, 424:439].dot(2**np.arange(population[:, 424:439].shape[1])[::-1])
	chrom29 = population[:, 440:455].dot(2**np.arange(population[:, 440:455].shape[1])[::-1])
	chrom30 = population[:, 456:471].dot(2**np.arange(population[:, 456:471].shape[1])[::-1])

	chrom1 = np.power(1.28* 2 / (2**16)  * chrom1 -1.28, 4) 
	chrom2 = 2*np.power(1.28 * 2 / (2**16) * chrom2-1.28, 4)
	chrom3 = 3*np.power(1.28 * 2 / (2**16) * chrom3-1.28 , 4)
	chrom4 = 4*np.power(1.28 * 2 / (2**16) * chrom4-1.28, 4)
	chrom5 = 5*np.power(1.28 * 2 / (2**16) * chrom5-1.28, 4) 
	chrom6 = 6*np.power(1.28* 2 / (2**16) * chrom6-1.28, 4 )
	chrom7 = 7*np.power(1.28 * 2 / (2**16) * chrom7-1.28, 4)
	chrom8 = 8*np.power(1.28 * 2 / (2**16) * chrom8-1.28, 4 )
	chrom9 = 9*np.power(1.28 * 2 / (2**16) * chrom9-1.28, 4)
	chrom10 = 10*np.power(1.28 * 2 / (2**16) * chrom10-1.28, 4 )
	chrom11 = 11*np.power(1.28* 2 / (2**16) * chrom11-1.28, 4) 
	chrom12 = 12*np.power(1.28 * 2 / (2**16) * chrom12-1.28, 4)
	chrom13 = 13*np.power(1.28 * 2 / (2**16) * chrom13-1.28, 4) 
	chrom14 = 14*np.power(1.28 * 2 / (2**16) * chrom14-1.28, 4)
	chrom15 = 15*np.power(1.28 * 2 / (2**16) * chrom15-1.28, 4) 
	chrom16 = 16*np.power(1.28* 2 / (2**16) * chrom16-1.28, 4) 
	chrom17 = 17*np.power(1.28 * 2 / (2**16) * chrom17-1.28, 4)
	chrom18 = 18*np.power(1.28 * 2 / (2**16) * chrom18-1.28, 4) 
	chrom19 = 19*np.power(1.28 * 2 / (2**16) * chrom19-1.28, 4)
	chrom20 =20* np.power(1.28 * 2 / (2**16) * chrom20-1.28, 4)
	chrom21 = 21* np.power(1.28* 2 / (2**16) * chrom21-1.28, 4) 
	chrom22 = 22* np.power(1.28 * 2 / (2**16) * chrom22-1.28, 4)
	chrom23 = 23* np.power(1.28 * 2 / (2**16) * chrom23-1.28, 4) 
	chrom24 = 24* np.power(1.28 * 2 / (2**16) * chrom24-1.28, 4)
	chrom25 = 25*np.power(1.28 * 2 / (2**16) * chrom25-1.28, 4) 
	chrom26 = 26*np.power(1.28* 2 / (2**16) * chrom26-1.28, 4) 
	chrom27 = 27*np.power(1.28 * 2 / (2**16) * chrom27-1.28, 4)
	chrom28 = 28*np.power(1.28 * 2 / (2**16) * chrom28-1.28, 4) 
	chrom29 = 29*np.power(1.28 * 2 / (2**16) * chrom29-1.28, 4)
	chrom30 = 30*np.power(1.28 * 2 / (2**16) * chrom30-1.28, 4)

	#print(chrom1)
	#val = np.random.randn(100, 30)
	#print(val)

	sumAll = 1250 - ((chrom1 + chrom2+chrom3+chrom4+chrom5+chrom6+chrom7+chrom8+chrom9+chrom10+chrom11+chrom12+chrom13+chrom14+chrom15+chrom16+chrom17+chrom18+chrom19+chrom20+chrom21+chrom22+chrom23+chrom24+chrom25+chrom26+chrom27+chrom28+chrom29+chrom30)) #+ np.random.randn(0,1))
	#print(sumAll)
	return sumAll

###########################################################################################################
# def proportional_distribution(population, sumAll)
# calculate the proportional distribution selection
# inputs: population, sumAll
# returns: newPop
############################################################################################################
def proportional_distribution(population, sumAll):
	total = np.sum(sumAll)

	probs = sumAll / total
	p = list(probs)
	
	l = []
	for i in range(100):
		l.append(i)
	chosen = []
	for i in range(len(l)):
		chosen.append(choice(l, p = p))
	

	newPop = []

	for i in range(len(chosen)):
		newPop.append(population[chosen[i], :])

	newPop = np.asarray(newPop)

	return newPop

###########################################################################################################
# def  crossover(population, rate)
# Perform crossover
# inputs: population, sumAll
# returns: l
############################################################################################################
def crossover(population, rate):
	l = []
	for i in range(100):
		if i % 2 == 0:
			c = choice([0,1], p=[1-rate, rate])
			if c ==1:
				val = random.randint(2, 46)
			
				chunk1a = population[i, :val]
				chunk1b = population[i, val:]
				chunk2a = population[i+1, :val]
				chunk2b = population[i+1, val:]
			

				chrom1 = np.concatenate((chunk1a, chunk2b), None)
				chrom2 = np.concatenate((chunk2a, chunk1b), None)
			else:
				chrom1 = population[i]
				chrom2 = population[i+1]	
			l.append(chrom1)
			l.append(chrom2)	

	return np.asarray(l)
###########################################################################################################
# def  mutate(population, rate)
# Perform mutation
# inputs: population, rate
# returns: mutPop
############################################################################################################
def mutate(population, rate):
	mutPop = population
	for i in range(100):
		for j in range(len(population[0])):
			#print(i,j)
			c= choice([0,1], p=[1-rate, rate])
			if c == 1:
				if mutPop[i, j] == 0:
					mutPop[i, j] =1
				else:
					mutPop[i, j]= 0


	return mutPop
###########################################################################################################
# def calculate(sumAll, e, avMin, avAv, avMax)
# Calculate the statistics
# inputs: sumAll, e, avMin, avAv, avMax
# returns: nothing
############################################################################################################
def calculate(sumAll, e, avMin, avAv, avMax):
	if len(avAv) < 50:
		avMin.append(np.min(sumAll))
		avMax.append(np.max(sumAll))
		avAv.append(np.mean(sumAll))
	else:
		avMin[e] +=np.min(sumAll)
		avMax[e] +=np.max(sumAll)
		avAv[e] +=np.mean(sumAll)	
###########################################################################################################
# def average(avMin, avMax, avAv)
# Calculate averages
# inputs: avMin, avMax, avAv
# returns: nothing
############################################################################################################
def average(avMin, avMax, avAv):
	for i in range(len(avMax)):
		avMin[i] = avMin[i] / 30
		avMax[i] = avMax[i] /30
		avAv[i] = avAv[i] /30
###########################################################################################################
# def plot(avMin, avMax, avAv, px, pm, dejong)
# plot stuff
# inputs: avMin, avMax, avAv, px, pm, dejong
# returns: nothing
############################################################################################################
def plot(avMin, avMax, avAv, px, pm, dejong):
	x_axis = []
	for i in range(1, 51):
		x_axis.append(i)
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)
	ax.plot(x_axis, avMin, label= 'Av Min')
	ax.plot(x_axis, avMax, label= 'Av Max')
	ax.plot(x_axis, avAv, label = 'Av Av')
	#ax.plot(x_axis, m, label= 'True Max')
	plt.xlabel('Generation')
	plt.ylabel('Average Fitness')
	plt.title(dejong + 'Fitnesses Px: ' + str(px) + ' Pm: ' + str(pm))
	plt.legend()
	plt.show()
###########################################################################################################
# def first(pop)
# run first dejong
# inputs: pop
# returns: nothing
############################################################################################################	
def first(pop):
	with open('first_dejong.csv', mode='w') as write:
		writer = csv.writer(write,   delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		#print("1")
		run = 0
		px = [.7, .7, .7, .3, 1]
		pm =[.001, .01, .0001, .001, .001]
		
		
		avMin =[]
		avAv= []
		avMax=[]
		for i in range(len(px)):
			#print("2)")
			while run < 30:
				#print("3")
				e = 0
				val = 1
				while e < 50:
					#print("4")
					sumAll =calculate_first_dejong(pop)
					calculate(sumAll, e, avMin, avAv, avMax)
					writer.writerow([e] + [px[i]] +[pm[i]])
					writer.writerow(sumAll)
					val = sumAll[1]
					#print(sumAll)
					pop = proportional_distribution(pop, sumAll)
					pop=crossover(pop, px[i])
					pop = mutate(pop, pm[i])
					e +=1
					writer.writerow([])
				run +=1
	
			average(avMin, avMax, avAv)
			#print(avMin)
			#print(avAv)
			#print(avMax)
			plot(avMin, avMax, avAv, px[i], pm[i], 'Dejong 1 ')
###########################################################################################################
# def second(pop)
# run second dejong
# inputs: pop
# returns: nothing
############################################################################################################	
def second(pop):
	with open('second_dejong.csv', mode='w') as write:
		writer = csv.writer(write, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		run = 0
		px = [.7, .7, .7, .3, 1.00]
		pm =[.001, .01, .0001, .001, .001]
		avMin =[]
		avAv= []
		avMax=[]
		for i in range(len(px)):
			while run < 30:
				e = 0
				while e < 50:
					sumAll =calculate_second_dejong(pop)
					#print(sumAll)
					calculate(sumAll, e, avMin, avAv, avMax)
					writer.writerow([e] + [px[i]] +[pm[i]])
					writer.writerow(sumAll)
					pop = proportional_distribution(pop, sumAll)
					pop=crossover(pop, px[i])
					pop = mutate(pop, pm[i])
					e +=1
				run +=1
			average(avMin, avMax, avAv)
			#print(avMin)
			#print(avAv)
			#print(avMax)
			plot(avMin, avMax, avAv, px[i], pm[i], 'Dejong 2 ')
###########################################################################################################
# def third(pop)
# run third dejong
# inputs: pop
# returns: nothing
############################################################################################################	
def third(pop):
	with open('third_dejong.csv', mode='w') as write:
		writer = csv.writer(write, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		run = 0
		px = [.7, .7, .7, .3, 1]
		pm =[.001, .01, .0001, .001, .001]
		avMin =[]
		avAv= []
		avMax=[]
		for i in range(len(px)):
			while run < 30:
				e = 0
				while e < 50:
					sumAll =calculate_third_dejong(pop)
					calculate(sumAll, e, avMin, avAv, avMax)
					writer.writerow([e] + [px[i]] +[pm[i]])
					writer.writerow(sumAll)
					pop = proportional_distribution(pop, sumAll)
					pop=crossover(pop, px[i])
					pop = mutate(pop, pm[i])
					e +=1
				run +=1
			average(avMin, avMax, avAv)
			#print(avMin)
			#print(avAv)
			#print(avMax)
			plot(avMin, avMax, avAv, px[i], pm[i], 'Dejong 3 ')
###########################################################################################################
# def fourth(pop)
# run fourth dejong
# inputs: pop
# returns: nothing
############################################################################################################	
def four(pop):
	with open('four_dejong.csv', mode='w') as write:
		writer = csv.writer(write, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		run = 0
		px = [.7, .7, .7, .3, 1]
		pm =[.001, .01, .0001, .001, .001]
		avMin =[]
		avAv= []
		avMax=[]
		for i in range(len(px)):
			while run < 30:
				e = 0
				while e < 50:
					sumAll =calculate_fourth_dejong(pop)
					calculate(sumAll, e, avMin, avAv, avMax)
					writer.writerow([e] + [px[i]] +[pm[i]])
					writer.writerow(sumAll)
					pop = proportional_distribution(pop, sumAll)
					pop=crossover(pop, px[i])
					pop = mutate(pop, pm[i])
					e +=1
				run +=1
			average(avMin, avMax, avAv)
			#print(avMin)
			#print(avAv)
			#print(avMax)
			plot(avMin, avMax, avAv, px[i], pm[i], 'Dejong 4 ')



def main():
	pop=generate_population1()
	first(pop)
	pop = generate_population2()
	second(pop)
	pop= generate_population3()
	third(pop)
	pop = generate_population4()
	four(pop)




if __name__ == "__main__":
	main()
