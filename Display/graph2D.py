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
            color: np.ndarray = None, title: str = "", 
            legend: np.ndarray or str = None, xLabel: str = None, 
            yLabel: str = None) -> plt.show:
    """
        Plot a 2D graph

        Parameter
        ---------
            xContainer  -> Abscissa axis container
            yContainer  -> Ordinate axis container
            color       -> Color Container
            title       -> Title of the graph
            legend      -> The legend of the graph
            xLabel      -> Abscissa label
            yLabel      -> Ordinate label

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
        plt.plot(xContainer, yContainer, color=color, label=legend)

    else:
        # If the color is not specified
        if color is None:
            # Default color
            color: np.ndarray = getRandomColor(
                numberGraph=len(xContainer))

        # Add as many graph as possible depending on xContainer
        list(
            map(
                lambda x, y, col, label: plt.plot(x, y, color=col, label=label),
                xContainer, yContainer, color, legend
            )
        )

    # Add label
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    
    # Add a title to the graph
    plt.title(title)
    
    # Add legend to the graph
    plt.legend()

    # Show the graph
    return plt.show()