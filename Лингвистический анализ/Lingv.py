
from PIL import ImageDraw, Image
import PIL
from math import sqrt, pow
from tkinter import *
from tkinter import messagebox
import glob, os, os.path

width = 200
height = 200
center = height//2
white = (255, 255, 255)
green = (0,128,0)

list_image = []


def find_left_lower_corner(matrix):
    for i in range(len(matrix) - 1, -1, -1):
        for j in range(0, len(matrix[i]), 1):
            if matrix[i][j] == 1:
                return (i, j)


# a - вправо
# b - вправо-вверх
# c - вверх
# d - влево-вверх
# e - влево
# f - влево-вниз
# g - вниз
# h - вправо-вниз

def do_DFS(img_matrix, traverse_matrix, i, j):
    height, width = len(img_matrix), len(img_matrix[0])
    traverse_matrix[i][j] = True
    left = j > 0
    up = i > 0
    right = j < width - 1
    down = i < height - 1

    traverse = ''
    multi = False

    symbols = ['+c', '+a', '+e', '+g']
    conds = [up, right, left, down, up and right, up and left, left and down, right and down]
    iS = [i - 1, i, i, i + 1, i - 1, i - 1, i + 1, i + 1]
    jS = [j, j + 1, j - 1, j, j + 1, j - 1, j - 1, j + 1]

    for q in range(len(symbols)):
        if conds[q] and img_matrix[iS[q]][jS[q]] == 1 and not (traverse_matrix[iS[q]][jS[q]]):
            if (multi):
                traverse += '+('
            traverse += symbols[q] + do_DFS(img_matrix, traverse_matrix, iS[q], jS[q])
            if (multi):
                traverse += ')'
            multi = True

    if up and right and img_matrix[i - 1][j + 1] == 1 and not (
            traverse_matrix[i - 1][j + 1] or traverse_matrix[i][j + 1]):
        if (multi):
            traverse += '('
        traverse += '+b' + do_DFS(img_matrix, traverse_matrix, i - 1, j + 1)
        if (multi):
            traverse += ')'
        multi = True
    if up and left and img_matrix[i - 1][j - 1] == 1 and not (
            traverse_matrix[i - 1][j - 1] or traverse_matrix[i][j - 1]):
        if (multi):
            traverse += '('
        traverse += '+d' + do_DFS(img_matrix, traverse_matrix, i - 1, j - 1)
        multi = True
    if left and down and img_matrix[i + 1][j - 1] == 1 and not (
            traverse_matrix[i + 1][j - 1] or traverse_matrix[i][j - 1]):
        if (multi):
            traverse += '('
        traverse += '+f' + do_DFS(img_matrix, traverse_matrix, i + 1, j - 1)
        if (multi):
            traverse += ')'
        multi = True
    if right and down and img_matrix[i + 1][j + 1] == 1 and not (
            traverse_matrix[i + 1][j + 1] or traverse_matrix[i][j + 1]):
        if (multi):
            traverse += '('
        traverse += '+h' + do_DFS(img_matrix, traverse_matrix, i + 1, j + 1)
        if (multi):
            traverse += ')'
        multi = True
    return traverse


def linguistic(im):
    img = PIL.Image.open(im)
    img_matrix = binarise_image(img)
    i_b, j_b = find_left_lower_corner(img_matrix)
    height, width = len(img_matrix), len(img_matrix[0])
    traverse_matrix = [[False for j in range(width)] for i in range(height)]
    traverse = do_DFS(img_matrix, traverse_matrix, i_b, j_b)
    traverse = traverse.replace('+', '', 1)
    traverse = traverse.replace('(+', '(', 1)
    print('a - вправо')
    print('b - вправо-вверх')
    print('c - вверх')
    print('d - влево-вверх')
    print('e - влево')
    print('f - влево-вниз')
    print('g - вниз')
    print('h - вправо-вниз')
    print(traverse)

def EuclideanDistance(a, b):
    return sum((a[i]-b[i])**2 for i in range(len(a)))**(0.5)

def pixel_to_bin(pixel):
    R, G, B = pixel
    return 1 if sqrt(R * R + G * G + B * B) < 128 else 0

def binarise_image(img):
    pixels = img.load()
    width, height = img.size
    return [[pixel_to_bin(pixels[j, i]) for j in range(width)] for i in range(height)]

i = 1

def r():
    def save():
        global i
        global cv
        filename = "image{}.jpg".format(i)
        image1.save(filename)
        if filename != "image0.jpg" : list_image.append(filename)
        i = i + 1
        root.quit()
        root1.destroy()

    def paint(event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        cv.create_oval(x1, y1, x2, y2, fill="black",width=5)
        draw.line([x1, y1, x2, y2],fill="black",width=5)


    root1 = Tk()

    cv = Canvas(root1, width=width, height=height, bg='white')
    cv.pack()

    image1 = PIL.Image.new("RGB", (width, height), white)
    draw = ImageDraw.Draw(image1)

    cv.pack(expand=YES, fill=BOTH)
    cv.bind("<B1-Motion>", paint)

    button=Button(root1,text="save",command=save)
    button.pack()
    root1.mainloop()


def add():
    r()

def test():
    global root
    root.quit()

def on_closing():
    filelist = glob.glob(os.path.join("*.jpg"))
    for f in filelist:
        os.remove(f)
    root.destroy()


root = Tk()
button = Button(root, text="Добавить рисунок", command=add)
button.pack()
button = Button(root, text="Построить лингв. анализ", command=test)
button.pack()
root.protocol("WM_DELETE_WINDOW", on_closing)
while True:
    root.mainloop()
    linguistic(list_image[0])
