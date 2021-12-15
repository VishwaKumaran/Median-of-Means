"""
// 
//	MOM.py
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
    
def MOM(data: list or np.ndarray, nbSplit: int) -> float:
    """
        Median of Means
        
        Calculate for each split his mean and
        take the median of it

        Parameter
        ---------
            data: np.ndarray or array
                The data sample
            
            nbSplit: int
                The number of split

        Return
        ------
            float
            MOM estimator
    """
    if nbSplit > len(data):
        nbSplit: int = int(
            np.ceil(len(data) / 2)
        )
#   elif len(data) == 1:
#       nbSplit: int = 1
        
    # Shuffle the sample
    splitIndex: np.ndarray = np.array(
        list(range(nbSplit)) * int(len(data) / nbSplit)
    )
    np.random.shuffle(splitIndex)
    
    
    # Calculate mean for each split
    means: list = np.array(
        [
            np.mean(
                data[
                    list(np.where(splitIndex == index)[0])
                ]
            ) for index in range(nbSplit)
        ]
    )
    
    # Return the median
    return np.median(means)

if __name__ == "__main__":
    import random
    
    population = np.random.normal(loc=0, size=1000, scale=1)
    print(MOM(population, 10))

    