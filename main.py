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
from Estimator.Mean import Mean
from Estimator.MOM import MOM
from Estimator.RobustMOM import RobustMOM

from MSE.MSE import MSE
from MSE.MSEBenchmark import MSEBenchmark

from Display.graph2D import graph2D

__author__ = "Vishwa ELANKUMARAN, Vincent SOGNO"
__copyright__ = "Copyright 2021, Median of Means pour le Deep Learning Robuste"
__version__ = "1.2"
__maintainer__ = "Vishwa ELANKUMARAN, Vincent SOGNO"
__email__ = "vishwa.elankumaran@univ-lyon2.fr, vincent.sogno@univ-lyon2.fr"
__status__ = "in development"

######################################################################
######################################################################
######################################################################

"""
	Calcul du risque quadratique de l'estimateur moyenne
"""
	

"""
	Calcul du risque quadratique de l'estimateur MOM
"""
	

######################################################################
######################################################################
######################################################################

""" 
	Comparatif de l'erreur entre l'estimateur moyenne/MOM/Robust MOM
	en fonction de la taille de l'échantillon (gaussien)
"""

N: int = 500

# Calcul du risque quadratique
# Initialisation
MSEContainer: np.ndarray = np.array(
	[np.zeros(N) for i in range(3)]
)

# Erreur quadratique pour l'estimateur moyenne
MSEContainer[0]: np.ndarray = np.array(
	[MSEBenchmark(Mean, N)]
)

# Erreur quadratique pour l'estimateur MOM
MSEContainer[1]: np.ndarray = np.array(
	[MSEBenchmark(MOM, N, 10)]
)

# Erreur quadratique pour l'estimateur Robust MOM
MSEContainer[2]: np.ndarray = np.array(
	[MSEBenchmark(RobustMOM, N, 10)]
)

# Affichage de l'évolution du MSE
graph2D(
	xContainer = np.array([np.arange(N) for i in range(3)]),
	yContainer = MSEContainer,
	# Blue pour l'estimateur moyenne et rouge pour l'estimateur MOM
	# Et noir pour MOM Robuste
	color = np.array(["steelblue", "red", "seagreen"]),
	title = "Evolution du MSE",
	legend = np.array(["Moyenne", "MOM", "Robust MOM"]),
	xLabel = "Itération",
	yLabel = "Mean Squared Error"
)

## Estimateur MOM et Roust MOM meilleur en général mais plus long à calculer "complexité"
#
#######################################################################
#######################################################################
#######################################################################