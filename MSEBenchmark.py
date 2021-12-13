"""
// 
//	MSEBenchmark.py
//	Median of Means pour le Deep Learning Robuste
//
//	Created by Vishwa Elankumaran on 13/12/2021.
//	Copyright © 2021 Vishwa Elankumaran. All rights reserved.
//
"""

# Packages
import numpy as np

# Files
from MSE import MSE

__author__ = "Vishwa ELANKUMARAN, Vincent SOGNO"
__copyright__ = "Copyright 2021, Median of Means pour le Deep Learning Robuste"
__version__ = "1.1"
__maintainer__ = "Vishwa ELANKUMARAN, Vincent SOGNO"
__email__ = "vishwa.elankumaran@univ-lyon2.fr, vincent.sogno@univ-lyon2.fr"
__status__ = "in development"

def MSEBenchmark(estimator, size: int = 1000, *args) -> np.ndarray:
    """
        Calculate the MSE for a given size of
        a sample

        Parameter
        ---------
            estimator -> The estimator function
            size      -> Size of the sample
            *args     -> Additional parameter coming
                         from the estimator function

        Return
        ------
            np.ndarray
            The MSE for each sample
    """
    # Sample
    XContainer: np.ndarray = np.array(
        # Loi Normale centree reduite
#       [np.random.normal(loc = 0, scale = 1, size = n) for n in range(1, N + 1)],
        
        # Loi de Student
        # Bizarre lorsque que df = 1 à voir pk
#       [np.random.standard_t(df = 10, size = n) for n in range(1, N + 1)],
        
        # Loi de Poisson
        [np.random.poisson(lam = 1, size = n) for n in range(1, size + 1)],
        dtype = object
    )
    
    theta: np.ndarray = np.array(
        [np.mean(XContainer[m]) for m in range(size)]
    )
    
    thetaHat: np.ndarray = np.array(
        [estimator(XContainer[m], *args) for m in range(size)]
    )
    
    return np.array(
        [MSE(theta[m], thetaHat[m]) for m in range(size)]
    )
    