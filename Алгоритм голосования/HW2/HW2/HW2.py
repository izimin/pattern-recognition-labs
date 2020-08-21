import Orange
data = Orange.data.Table("wine")

eps = 0.5

def G(wineClass, S, w):
    k = 0
    for d in data:
        if d[len(d)-1] == wineClass:
            if abs(w[S]-d[S]) < eps:
                k = k+1
    return k

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
            print("Алкоголь: ", end=''); 
            alcohol = float(input())
            print("Яблочная кислота: ", end='')
            malicAcid = float(input())
            print("Щелочь: ", end='')
            ash = float(input())
            print("Содержание щелочи: ", end='')
            alcalinityOfAsh = float(input())
            print("Магний: ", end='')
            magnesium = float(input())
            print("Всего фенолов: ", end='')
            totalPhenols = float(input())
            print("Флавоноиды: ", end='')
            flavanoids = float(input())
            print("Нефлаваноиды фенолы: ", end='')
            nonflavanoidsPhenols = float(input())
            print("Проантоцианидины: ", end='')
            proanthocyanins = float(input())
            print("Интенсивность цвета: ", end='')
            colorIntensity = float(input())
            print("Оттенок: ", end='')
            hue = float(input())
            print("OD280: ", end='')
            OD280 = float(input())
            print("Пролин: ", end='')
            proline = float(input())
            n = [alcohol, malicAcid, ash, alcalinityOfAsh, magnesium, totalPhenols, flavanoids, nonflavanoidsPhenols, proanthocyanins, colorIntensity, hue, OD280, proline]
print ("\nВсе критерии независимы, поэтому будем считать S1 = x1, S2 = x2, ..., S14 = x14")
print ("\nОбраз для распознавания: ", n)
minED = float("inf"); minHD = float("inf"); minDB = float("inf")
wineED = 0; wineHD = 0; wineDB = 0
stED = []; stHD = []; stDB = []

max = -1
res = '0'
for cl in "123":
    sumG = 0
    for S in range(0, len(data[0])-1):
        sumG = sumG + G(cl, S, n)
    print("Г(w',",cl,") = ",sumG)
    if sumG > max:
        max = sumG
        res = cl
print ("Сорт вина: ", res)

