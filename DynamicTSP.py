#This program uses dynamic programing to solve TSP problem
from sys import maxsize 
from itertools import permutations

#number of nodes
cities = 4
 
# function to implement TSP
def TSP(): 
 
    # keep all vertex other than the starting point
    vertex = [] 

    #traverse the diagram 
    for i in range(cities): 
        if i != s: 
            vertex.append(i) 
 
    # keep minimum weight path
    min_path = maxsize 
    
    next_permutation = permutations(vertex)
    best_path = []
    
    for i in next_permutation:
        # store current path cost
        current_pathweight = 0
        
        # procress current path weight 
        k = s 
        for j in i: 
            current_pathweight += graph[k][j] 
            k = j 
        current_pathweight += graph[k][s] 
        
        # update minimum 
        if current_pathweight < min_path:
            min_path = current_pathweight
            best_path = [s]
            best_path.extend(list(i))
            best_path.append(s)
    
    print("BEST PATH IS:\n",best_path)
    print("LOWEST COST IS:")
    return min_path

# Driver Code 
if __name__ == "__main__":
 
    #graph representation of the four nodes
    graph = [[0, 10, 15, 20], 
             [10, 0, 35, 25], 
             [15, 35, 0, 30], 
             [20, 25, 30, 0]
            ] 
    s = 0

    print(TSP())
