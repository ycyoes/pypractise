import numpy as np
from scipy.stats import poisson

def shannon_entropy(p_x):
    return - np.sum(p_x * np.log(p_x))

poi = poisson(10.0)
n = 100
pmf = poi.pmf(np.arange(n))

print(poi.entropy())








