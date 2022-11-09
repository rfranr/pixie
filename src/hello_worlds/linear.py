import numpy as np

def cross_vector(v1:list[int], v2:list[int]) -> list[int]:
    v3 = np.cross(v1,v2)
    return v3.tolist()

def cross_vector(v1:list[float], v2:list[float]) -> list[float]:
    v3 = np.cross(v1,v2)
    return v3.tolist()
