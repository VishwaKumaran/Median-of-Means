"""
// 
//	Mean.py
//	Median of Means pour le Deep Learning Robuste
//
//	Created by Vishwa Elankumaran on 13/12/2021.
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

def Mean(data: list or np.ndarray) -> float:
    """
        Mean
        
        Calculate the mean of a sample
        which is shuffled

        Parameter
        ---------
            data: np.ndarray or array
                The data sample

        Return
        ------
            float
            Mean estimator
    """
    return np.mean(
        np.random.choice(data, size = len(data), replace = True)
    )