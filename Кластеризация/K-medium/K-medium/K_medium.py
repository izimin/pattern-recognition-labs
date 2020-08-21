import Orange
data = Orange.data.Table("wine")
#data = [[0,0],[3,8],[2,2],[1,1],[5,3],[4,8],[6,3],[5,4],[7,5]]
#data = [[0,0],[1,0],[0,1],[1,1],[2,1],[1,2],[2,2],[3,2],[5,5],[5,6],[6,5],[7,5],[6,6],[7,6],[8,6],[8,7],[7,7],[6,7],[8,8],[7,8]]

def EuclideanDistance(a, b):
    return sum((a[i]-b[i])**2 for i in range(len(a)))**(0.5)
     
def GetListClusters(z, data):
	clusters = [ [] for i in range(len(z))]
	for elem in data:
		listd = list(EuclideanDistance(z[i], elem) for i in range(len(z)))
		clusters[listd.index(min(listd))].append(elem)
	return clusters

def add(x, y):
	return list(map(lambda a, b: a + b, x, y))

for elem in data: print(elem)

print("Введите число кдастеров K: ")
k = int(input())
z = [data[i] for i in range(k)]
n = 1
while True:
	print ("-------")
	for iz in range(len(z)):
		print("z({})_{} = {}".format(n, iz+1, z[iz]))
	print ("-------")
	clusters = GetListClusters(z, data)
	for ic in range(len(clusters)):
		print("Элементы кластера №", ic+1)
		for el in clusters[ic]:
			print(el)
		print("------")
	f = False
	for i in range(k):
		summ = clusters[i][0]
		for e in range(1, len(clusters[i])):
			summ = add(summ, clusters[i][e])
		summ = list(map(lambda a: round(a/(len(clusters[i]))*100)/100, summ))
		if summ != z[i]: 
			f = True
			z[i] = summ
	n = n+1
	if f != True: break