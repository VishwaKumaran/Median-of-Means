"""
// 
//	main.py
//	Median of Means pour le Deep Learning Robuste
//
//	Created by Vishwa Elankumaran on 06/12/2021.
//	Copyright © 2021 Vishwa Elankumaran. All rights reserved.
//
"""

# Packages
import numpy as np
import random

# Files
from MSE import MSE
from MOM import MOM
from Display.graph2D import graph2D

__author__ = "Vishwa ELANKUMARAN, Vincent SOGNO"
__copyright__ = "Copyright 2021, Median of Means pour le Deep Learning Robuste"
__version__ = "1.1"
__maintainer__ = "Vishwa ELANKUMARAN, Vincent SOGNO"
__email__ = "vishwa.elankumaran@univ-lyon2.fr, vincent.sogno@univ-lyon2.fr"
__status__ = "in development"


## Calcul du risque quadratique de l'estimateur moyenne
#y: np.ndarray = np.zeros(10000)
#y_pred: np.ndarray = np.zeros(10000)
#
#for iter in range(10000):
#	# Echantillon
#	sample: np.ndarray = np.random.normal(
#		loc = 0, scale = 1, size = 10000
#	)
#	
#	shuffle: np.ndarray = np.random.choice(
#		sample, size = 10000
#	)
#	
#	# Moyenne des échantillon
#	y[iter]: float = np.mean(sample)
#	y_pred[iter]: float = np.mean(shuffle)
#	
#print(
#	MSE(y, y_pred)
#) # 9.987324808726606e-05
#
## Calcul du risque quadratique de l'estimateur MOM
#for iter in range(1000):
#	# Echantillon
#	sample: np.ndarray = np.random.normal(
#		loc = 0, scale = 1, size = 10000
#	)
#	
#	# Moyenne des échantillon
#	y[iter]: float = np.mean(sample)
#	y_pred[iter]: float = MOM(sample, 100)
#	
#print(
#	MSE(y, y_pred)
#) # 9.52413586694907e-05

# Comparatif de l'erreur entre l'estimateur moyenne et MOM
# en fonction de la taille d'échantillon

nbSamples: int = 1000

# La premiere liste sera pour les moyennes et la
# deuxième liste sera pour la MOM
MSEContainer: np.ndarray = np.array(
	[np.zeros(nbSamples) for i in range(2)]
)

y: np.ndarray = np.zeros(nbSamples)
y_predMean: np.ndarray = np.zeros(nbSamples)
y_predMOM: np.ndarray = np.zeros(nbSamples)

sample: np.ndarray = np.random.normal(
	loc = 0, scale = 1, size = nbSamples
)

shuffle: np.ndarray = np.random.choice(
	sample, size = nbSamples
)

for nbSample in range(1, nbSamples):
	# Moyenne des échantillon
	y[nbSample]: float = np.mean(sample[:nbSample])
	y_predMean[nbSample]: float = np.mean(shuffle[:nbSample])
	y_predMOM[nbSample]: float = MOM(sample[:nbSample], 10)
	
	MSEContainer[0][nbSample]: float = MSE(y[:nbSample], y_predMean[:nbSample])
	MSEContainer[1][nbSample]: float = MSE(y[:nbSample], y_predMOM[:nbSample])
	

graph2D(
	xContainer = np.array([np.arange(nbSamples) for i in range(2)]),
	yContainer = MSEContainer,
	title = "Evolution du MSE"
)

