import numpy as np
from typeguard import typechecked
from typing import TypeAlias

Vector: TypeAlias = list[float|int]

@typechecked
def cross_vector(v1:Vector, v2:Vector) -> Vector:
    v3 = np.cross(v1,v2)
    return v3.tolist()
