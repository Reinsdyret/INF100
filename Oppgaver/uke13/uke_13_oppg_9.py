#Lars Haukland Uke13 Numpy
import numpy as np

arr = np.arange(42,59)
new_arr = np.where(arr % 2 == 0,arr,1)

print(new_arr)
