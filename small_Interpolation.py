from scipy.interpolate import interp1d
import numpy as np

xs = [10, 15]
ys = [5040, 5160]

interp_func = interp1d(xs, ys)

newarr = interp_func(11)

print(newarr)
