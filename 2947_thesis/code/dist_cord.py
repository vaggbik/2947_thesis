import math
for i in range(0, len(x)):
    for j in range(0, len(y)): 
        if i!=j:
            eq=(x[j]-x[i])**2 + (y[j]-y[i])**2
            distance[i,j] = math.sqrt(eq)