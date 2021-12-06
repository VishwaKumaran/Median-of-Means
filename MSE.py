"""
// 
//	MSE.py
//	Median of Means pour le Deep Learning Robuste
//
//	Created by Vishwa Elankumaran on 01/12/2021.
//	Copyright © 2021 Vishwa Elankumaran. All rights reserved.
//
"""

# Packages
import numpy as np

__author__ = "Vishwa ELANKUMARAN, Vincent SOGNO"
__copyright__ = "Copyright 2021, Median of Means pour le Deep Learning Robuste"
__version__ = "1.1"
__maintainer__ = "Vishwa ELANKUMARAN, Vincent SOGNO"
__email__ = "vishwa.elankumaran@univ-lyon2.fr, vincent.sogno@univ-lyon2.fr"
__status__ = "in development"

def MSE(theta: np.ndarray, thetaHat: np.ndarray) -> float:
	"""
		Mean Squared Error
		
		Measure the quality of an estimator.
		Calculate the average squared between the estimated
		values and the actual value.

		Parameter
		---------
			theta: np.ndarray or array
				Target values
			
			thetaHat: np.ndarray or array
				Estimated target values

		Return
		------
			float
			Average of the squared of the errors
	"""
	return np.square(
		np.subtract(theta, thetaHat)
	).mean()
	
if __name__ == "__main__":
	ech = np.random.normal(size = 1000)
	ech_pred = [np.mean(np.random.choice(ech)) for i in range(1000)]

	print(MSE(ech, ech_pred))
		
		
	
	y: list = [5, -2, 2, 1]
	y_pred: list = [5.6, -1.6, 1.9, 0.9]
	
	print(MSE(y, y_pred))