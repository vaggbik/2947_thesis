distance= (distance + distance.T)/2
distance= distance.astype(int)
for i in range(0,areas):
    distance[i,i]=0