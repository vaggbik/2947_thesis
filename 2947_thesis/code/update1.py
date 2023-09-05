#returning each ant to its original area
for i in range(len(ant_areas)):
    ant_distances[i] += distance[ant_areas[i][0]][ant_areas[i][4]]
    ant_areas[i].append(ant_areas[i][0])
