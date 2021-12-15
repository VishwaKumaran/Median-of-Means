"""
// 
//	RobustMOM.py
//	Median of Means pour le Deep Learning Robuste
//
//	Created by Vishwa Elankumaran on 13/12/2021.
//	Copyright © 2021 Vishwa Elankumaran. All rights reserved.
//
"""

# Packages
import numpy as np

# Files
from Estimator.MOM import MOM

__author__ = "Vishwa ELANKUMARAN, Vincent SOGNO"
__copyright__ = "Copyright 2021, Median of Means pour le Deep Learning Robuste"
__version__ = "1.1"
__maintainer__ = "Vishwa ELANKUMARAN, Vincent SOGNO"
__email__ = "vishwa.elankumaran@univ-lyon2.fr, vincent.sogno@univ-lyon2.fr"
__status__ = "in development"

def RobustMOM(data: list or np.ndarray, nbSplit: int) -> float:
	"""
		Robust Median of Means
		
		Calculate for each split his mean and
		take the median of it. Then to make it
		robust repeat that x times and take his
		average

		Parameter
		---------
			data: np.ndarray or array
				The data sample
			
			nbSplit: int
				The number of split

		Return
		------
			float
			Robust MOM estimator
	"""
	return np.mean(
		[MOM(data, nbSplit) for i in range(nbSplit)]
	)