for ant in ant_areas:
    while len(ant) < areas:
        area=ant[-1]
        available_areas=[a for a in range(areas) if a not in ant] 
        probabilities=[(pheromone[area][a] ** alpha)*(distance[area][a] ** beta) for a in available_areas]
        total_pheromone=sum(probabilities)
        probabilities=[prob/total_pheromone for prob in probabilities]
        next_area=available_areas[roulette_wheel_select(probabilities)]
        ant.append(next_area)
ant_distances=[]
for ant in ant_areas:
    this_distance=0
    for i in range(len(ant)-1):
        this_distance += distance[ant[i]][ant[i+1]]
    ant_distances.append(this_distance)
print(ant_distances)


