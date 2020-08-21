
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

def EuclideanDistance(a, b):
    return sum((a[i]-b[i])**2 for i in range(len(a)))**(0.5)

def pixel_to_bin(pixel):
    R, G, B = pixel
    return 1 if sqrt(R * R + G * G + B * B) < 128 else 0

def binarise_image(img):
    pixels = img.load()
    width, height = img.size
    return [[pixel_to_bin(pixels[j, i]) for j in range(width)] for i in range(height)]

def calc_potentials(img):
    #img.show()
    matrix = binarise_image(img)
    height, width = len(matrix), len(matrix[0])
    potentials = []
    for i in range(height):
        potentials.append([])
        for j in range(width):
            potential = matrix[i][j]
            left = j > 0
            up = i > 0
            right = j < width - 1
            down = i < height - 1
            if left:
                potential += matrix[i][j - 1] * 0.5
            if left and up:
                potential += matrix[i - 1][j - 1] * 0.5
            if up:
                potential += matrix[i - 1][j] * 0.5
            if up and right:
                potential += matrix[i - 1][j + 1] * 0.5
            if right:
                potential += matrix[i][j + 1] * 0.5
            if right and down:
                potential += matrix[i + 1][j + 1] * 0.5
            if down:
                potential += matrix[i + 1][j] * 0.5
            if left and down:
                potential += matrix[i + 1][j - 1] * 0.5
            potentials[i].append(potential)
    return potentials


def calc_img_distance(img_pots_mat1, img_pots_mat2):
    if len(img_pots_mat1) != len(img_pots_mat2):
        return
    return sqrt(sum(pow(EuclideanDistance(img_pots_mat1[i], img_pots_mat2[i]), 2) for i in range(len(img_pots_mat1))))

res = "Расстояния: "
def potetntials(names):
    base_pots = calc_potentials(PIL.Image.open("image0.jpg"))
    N = len(names)
    images_potentials = [calc_potentials(PIL.Image.open(names[i])) for i in range(N)]
    distances = [calc_img_distance(base_pots, images_potentials[i]) for i in range(N)]

    for i in range(N):
        global res
        res = "{} {}".format(res, "\nРасстояние до изображения " + str(names[i]) + ": " + str(distances[i]))
    res = "{} {}".format(res, "\nТестовый образ относится к: " + names[distances.index(min(distances))])
    messagebox.showinfo("Результат", res)
    res = "Расстояния: "
    PIL.Image.open(names[distances.index(min(distances))]).show()
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
    global i
    global root
    i=0
    r()
    root.quit()

def on_closing():
    filelist = glob.glob(os.path.join("*.jpg"))
    for f in filelist:
        os.remove(f)
    root.destroy()

root = Tk()
button = Button(root, text="Добавить обуч. рисунок", command=add)
button.pack()
button = Button(root, text="Тест", command=test)
button.pack()
root.protocol("WM_DELETE_WINDOW", on_closing)
while True:
    root.mainloop()
    potetntials(list_image)


