for i in range(areas):
    for j in range(areas):
        if i!=j:
            pheromone[i][j] = 0.5*pheromone[i][j]+pheromone_sum[i][j]