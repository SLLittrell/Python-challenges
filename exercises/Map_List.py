# Write a function that takes two parameters. The first parameter should be a list of lists. 
# The second should be a lambda function. 
# The function should map the lambda function over the contents of the inner lists

def map_it(inp, func):
    result=[]
    for item in inp:
        result.append(list(map(func, item)))
    return result   

def test_map_it_solution():
     numbers = [[1,2,3,4], [5,6,7,8,9], [0,2,4]]

     letters = [['h', 'E', 'l', 'L', 'O'], ['w', 'O', 'r', 'L', 'd']]
     
     assert map_it(numbers, lambda x: x + 1) == [[2,3,4,5], [6,7,8,9,10], [1,3,5]]
     assert map_it(letters, lambda x: x.upper()) == [['H', 'E', 'L', 'L', 'O'], ['W', 'O', 'R', 'L', 'D']]
     assert map_it(numbers, lambda x: x ** 2) == [[1,4,9,16],[25,36,49,64,81],[0,4,16]]
     assert map_it(letters, lambda x: x.lower()) == [['h', 'e', 'l', 'l', 'o'], ['w', 'o', 'r', 'l', 'd']]