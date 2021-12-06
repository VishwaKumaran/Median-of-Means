"""
// 
//	getRandomColor.py
//	Median of Means pour le Deep Learning Robuste
//
//	Created by Vishwa Elankumaran on 06/12/2021.
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

def getRandomColor(numberGraph: int) -> np.ndarray:
    """
        Get a random color

        Parameter
        ---------
            numberGraph: int
                Number of graph

        Return
        ------
            float
            MOM estimator
    """
    return np.array(
        [np.random.rand(3,) for graph in range(numberGraph)]
    )   