#Lars Haukland Uke13 Numpy
import numpy as np

arr = np.arange(42,59)
print(arr[arr % 2 != 0])