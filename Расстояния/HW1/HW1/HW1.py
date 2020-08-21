import Orange
data = Orange.data.Table("wine")

def EuclideanDistance(a, b):
    sum = 0
    for i in range(len(a)):
        sum = sum + (a[i]-b[i])**2
    return sum**(0.5)

def HammingDistance(a, b):
    sum = 0
    for i in range(len(a)):
        sum = sum + abs(a[i]-b[i])
    return sum

def DistanceCityBlocks(a, b):
    max = 0
    for i in range(len(a)):
        ab = abs(a[i]-b[i])
        if ab > max:
            max = ab
    return ab

n1 = [15, 2, 2.7, 18.6, 110, 2.60, 2.8, 1.31, 1.5, 5, 1.1, 3.8, 1300]
n2 = [13, 1.7, 1.5, 24, 100, 2.74, 3.8, 0.4, 1.8, 5, 0.79, 2.9, 400]
n3 = [14, 4, 2.6, 25.4, 95, 1.4, 0.4, 0.72, 1.25, 6.9, 0.85, 1.75, 550]
n = 0
print("1)", n1, "\n2)", n2, "\n3)", n3)
print("Введите номер образа, который вы хотели бы распознать или любую другую клавишу, если хотите ввести образ сами.")
v = input()
if v == "1": n = n1
else: 
    if v == "2": n = n2
    else : 
        if v == "3": n = n3
        else :
            print("Алкоголь: ", end='');              alcohol = float(input())
            print("Яблочная кислота: ", end='');      malicAcid = float(input())
            print("Щелочь: ", end='');                ash = float(input())
            print("Содержание щелочи: ", end='');     alcalinityOfAsh = float(input())
            print("Магний: ", end='');                magnesium = float(input())
            print("Всего фенолов: ", end='');         totalPhenols = float(input())
            print("Флавоноиды: ", end='');            flavanoids = float(input())
            print("Нефлаваноиды фенолы: ", end='');   nonflavanoidsPhenols = float(input())
            print("Проантоцианидины: ", end='');      proanthocyanins = float(input())
            print("Интенсивность цвета: ", end='');   colorIntensity = float(input())
            print("Оттенок: ", end='');               hue = float(input())
            print("OD280: ", end='');                 OD280 = float(input())
            print("Пролин: ", end='');                proline = float(input())
            n = [alcohol, malicAcid, ash, alcalinityOfAsh, magnesium, totalPhenols, flavanoids, nonflavanoidsPhenols, proanthocyanins, colorIntensity, hue, OD280, proline]

print ("\nОбраз для распознавания: ", n, "\n\n")
minED = float("inf"); minHD = float("inf"); minDB = float("inf")
wineED = 0; wineHD = 0; wineDB = 0
stED = []; stHD = []; stDB = []

for elem in data:
    ed = EuclideanDistance(n, elem)
    hd = HammingDistance(n, elem)
    db = DistanceCityBlocks(n, elem)
    print (elem, " || E: %.3f" % ed, "  H: %.3f" % hd, "  B:  %.3f" % db)
    if ed < minED:         
        minED = ed; wineED = elem[len(elem)-1]; stED = elem
    if hd < minHD:
        minHD = hd; wineHD = elem[len(elem)-1]; stHD = elem
    if db < minDB:
        minDB = db; wineDB = elem[len(elem)-1]; stDB = elem
print ("\n\nМинимальное Евклидово расстояние: %.3f" % minED, "\nДостигается при наборе: ", stED, "\nCорт вина: ", wineED)
print ("\n\nМинимальное расстояние по Хеммингу: %.3f" % minHD, "\nДостигается при наборе: ", stHD, "\nCорт вина: ", wineHD)
print ("\n\nМинимальное расстояние городских кварталов: %.3f" % minDB, "\nДостигается при наборе: ", stDB, "\nCорт вина: ", wineDB)
