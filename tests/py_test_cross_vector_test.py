# test_capitalize.py
from src.core.math import linear   
import types


def test_crossvector_case():
    v1=[1,2,3]
    v2=[3,1,2]
    v3=linear.cross_vector(v1,v2)
    assert type(v3[0]) is int
    
def test_crossvector_case_float():
    v1=[1,2,3.9]
    v2=[3,1,2]
    v3=linear.cross_vector(v1,v2)
    assert type(v3[0]) is float
    
    