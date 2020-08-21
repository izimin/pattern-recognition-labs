import Orange
data = Orange.data.Table("wine")
#data = [[0,0],[3,8],[2,2],[1,1],[5,3],[4,8],[6,3],[5,4],[7,5]]

def EuclideanDistance(a, b):
    return sum((a[i]-b[i])**2 for i in range(len(a)))**(0.5)
     
for elem in data: print(elem)

print ("\nОбозначим центором первого кластера набор №1\nz 1 = ", data[0])
z = [data[0]]
while True:
	max = 0.
	maxEl = data[0]
	for elem in data:
		if elem in z: continue
		minn = min(EuclideanDistance(zE, elem) for zE in z)
		if minn > max: 
			max = minn
			maxEl = elem

	avg = sum(EuclideanDistance(z[i], z[j]) for i in range(len(z)) for j in range(i+1,len(z)))/len(z)

	if max > avg: 
		z.append(maxEl)
		print ("\nz", len(z)," = ", maxEl)
	else: break

clusters = [ [] for i in range(len(z))]

for elem in data:
	listd = list(EuclideanDistance(z[i], elem) for i in range(len(z)))
	clusters[listd.index(min(listd))].append(elem)


k = 0
for i in range(len(z)):
	print("\n----------------------------\nЭлементы", i+1, "-го кластера:\n")
	for e in clusters[i]: 
		print(e)
		if e[len(e)-1] != i+1: k = k+1

print ("Количество ошибок второго рода: ", k)