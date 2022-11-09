# hello_normal_vector_to_a_plane.py
from core.math.linear import cross_vector, Vector

# def cross_vector(vector):
#     print("g")
#     print(vector)

class Learning():

    def __init__(self):

        vector_one : Vector = [1, 2, 3]
        vector_two = [3, 2, 1]
        vector_three = cross_vector(vector_one, vector_two)
        print( vector_three )
        print ( type(vector_one))
        print ( type(vector_two))
        print ( type(vector_three))

        vector_one_f = [1.0, 2.2, 3.1]
        vector_two_f = [3.5, 2.6, 1.2]
        vector_three_f = cross_vector(vector_one_f, vector_two_f)
        print( vector_three_f )
        print ( type(vector_one_f))
        print ( type(vector_two_f))
        print ( type(vector_three_f))




