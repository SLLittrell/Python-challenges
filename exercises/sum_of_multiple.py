# Write a function that that takes a positive integer as a parameter. 
# The function should return the sum of all the multiples of 3 and/or 
# 5 less than (but not equal to) the number passed in

def sum_of_multiples(num):
    if num >= 0:
        a = list(range(3,(5 * 3)+1, 3))
        numbers = []
        for item in a:
         

def test_sum_of_multiples_solution():
    assert sum_of_multiples(10) == 23
    assert sum_of_multiples(20) == 78
    assert sum_of_multiples(0) == 0
    assert sum_of_multiples(1) == 0
    assert sum_of_multiples(200) == 9168
    assert sum_of_multiples(64) == 933