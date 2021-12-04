#!/usr/bin/env python3

import numpy as np

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
	y: list = [5, -2, 2, 1]
	y_pred: list = [5.6, -1.6, 1.9, 0.9]
	
	print(MSE(y, y_pred))