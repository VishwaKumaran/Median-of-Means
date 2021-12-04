#!/usr/bin/env python3

import numpy as np
import random

np.random.seed(12)

def _median_of_means(seq, n_blocks):
        """
        1. If clause to prevent n_blocks > n_observations
        2. Dividing data in n_blocks random blocks by generating numbers 0 to n_blocks obs per block times & shuffle
        3. List comp to iterate blocks, in each iteration we index from the total sequence the items that have been
            selected for class i, then we compute the empirical mean over these
        4. We return the median over the list of means
        """
        if n_blocks > len(seq):  # preventing the n_blocks > n_observations
            n_blocks = int(np.ceil(len(seq) / 2))
    
        # dividing seq in k random blocks
        indic = np.array(list(range(n_blocks)) * int(len(seq) / n_blocks))
        np.random.shuffle(indic)
    
        # computing and saving mean per block
        means = [np.mean(seq[list(np.where(indic == block)[0])]) for block in range(n_blocks)]
    
        # return median
        return np.median(means)


population = np.random.normal(loc=0, size=1000, scale=1)
sample = random.choices(population, k=100)
print(_median_of_means(population, 10))
print(np.mean(population))
print((np.mean(population)-_median_of_means(population, 10))**2)