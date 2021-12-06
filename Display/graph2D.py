"""
// 
//	graph2D.py
//	Median of Means pour le Deep Learning Robuste
//
//	Created by Vishwa Elankumaran on 06/12/2021.
//	Copyright © 2021 Vishwa Elankumaran. All rights reserved.
//
"""

# Packages
import numpy as np
import seaborn as sns

from matplotlib import pyplot as plt

# Files
from Display.getRandomColor import getRandomColor

__author__ = "Vishwa ELANKUMARAN, Vincent SOGNO"
__copyright__ = "Copyright 2021, Median of Means pour le Deep Learning Robuste"
__version__ = "1.1"
__maintainer__ = "Vishwa ELANKUMARAN, Vincent SOGNO"
__email__ = "vishwa.elankumaran@univ-lyon2.fr, vincent.sogno@univ-lyon2.fr"
__status__ = "in development"

def graph2D(xContainer: np.ndarray, yContainer: np.ndarray,
            color: np.ndarray = None, title: str = "") -> plt.show:
    """
        Plot a 2D graph

        Parameter
        ---------
            xContainer  -> Abscissa axis container
            yContainer  -> Ordinate axis container
            color       -> Color Container
            title       -> Title of the graph

        Return
        ------
            Display a 2D graph
    """
    sns.set()
    
    if not hasattr(xContainer[0], "__len__"):
        # If the color is not specified
        if color is None:
            # Default color
            color: np.ndarray = getRandomColor(numberGraph=1)

        # Add a graph
        plt.plot(xContainer, yContainer, color=color)

    else:
        # If the color is not specified
        if color is None:
            # Default color
            color: np.ndarray = getRandomColor(
                numberGraph=len(xContainer))

        # Add as many graph as possible depending on xContainer
        list(
            map(
                lambda x, y, col: plt.plot(x, y, color=col),
                xContainer, yContainer, color
            )
        )

    # Add a title to the graph
    plt.title(title)

    # Show the graph
    return plt.show()