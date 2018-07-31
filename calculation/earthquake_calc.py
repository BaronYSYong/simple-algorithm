"""
Eartquake Formulae : 
log E = 4.8 + (1.5*Magnitude)
"""

import math

def earthquake_energy(magnitude):
	"""
	return Energy in Joule
	"""
	return 10**(4.8+1.5*magnitude)

def earthquake_diff(magnitude1, magnitude2):
	"""
	return the ratio of 2 different magnitude
	"""
	return earthquake_energy(magnitude2)/earthquake_energy(magnitude1)
