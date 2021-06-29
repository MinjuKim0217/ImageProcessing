from tkinter import *
import tkinter
import cv2
import numpy as np
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk


def histogram_equal():
    global src
    # scr 변수 가져오기
    hist, bins = np.histogram(src.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_m = np.ma.masked_equal(cdf, 0)

    cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')

    img2 = cdf[src]

    fin_img = Image.fromarray(img2)
    imgtk = ImageTk.PhotoImage(image=fin_img)
    label.config(image=imgtk)
    label.image = imgtk


def nega():
    global src
    img_negative = 255 - src
    titles = ['img', 'Negative']
    images = [src, img_negative]

    fin_img = Image.fromarray(images)
    imgtk = ImageTk.PhotoImage(image=fin_img)
    label.config(image=imgtk)
    label.image = imgtk


def pow_law():
    global src
    gamma_two_point_two = np.array(255*(src/255)**2.2, dtype='uint8')
    gamma_point_four = np.array(255*(src/255)**0.4, dtype='uint8')
    img3 = cv2.hconcat([gamma_two_point_two, gamma_point_four])

    fin_img = Image.fromarray(img3)
    imgtk = ImageTk.PhotoImage(image=fin_img)
    label.config(image=imgtk)
    label.image = imgtk


def gaus():
    global src
    blur = cv2.GaussianBlur(src, (3, 3), 0)
    fin_img = Image.fromarray(blur)
    imgtk = ImageTk.PhotoImage(image=fin_img)
    label.config(image=imgtk)
    label.image = imgtk


def medi():
    global src
    blur = cv2.medianBlur(src, 5)
    fin_img = Image.fromarray(blur)
    imgtk = ImageTk.PhotoImage(image=fin_img)
    label.config(image=imgtk)
    label.image = imgtk


def aver():
    global src
    img_average = src.copy()

    k_size = 10
    average = cv2.blur(img_average, (k_size, k_size))

    fin_img = Image.fromarray(average)
    imgtk = ImageTk.PhotoImage(image=fin_img)
    label.config(image=imgtk)
    label.image = imgtk


def Robert():
    global src
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    roberts_x = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 0]])
    roberts_y = np.array([[0, 0, -1], [0, 1, 0], [0, 0, 0]])

    roberts_x = cv2.convertScaleAbs(cv2.filter2D(gray, -1, roberts_x))
    roberts_y = cv2.convertScaleAbs(cv2.filter2D(gray, -1, roberts_y))

    roberts = cv2.addWeighted(roberts_x, 1, roberts_y, 1, 0)

    fin_img = Image.fromarray(roberts)
    imgtk = ImageTk.PhotoImage(image=fin_img)
    label.config(image=imgtk)
    label.image = imgtk


def Prewitt():
    global src
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    prewitt_x = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
    prewitt_y = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])

    prewitt_x = cv2.convertScaleAbs(cv2.filter2D(gray, -1, prewitt_x))
    prewitt_y = cv2.convertScaleAbs(cv2.filter2D(gray, -1, prewitt_y))

    prewitt = cv2.addWeighted(prewitt_x, 1, prewitt_y, 1, 0)

    fin_img = Image.fromarray(prewitt)
    imgtk = ImageTk.PhotoImage(image=fin_img)
    label.config(image=imgtk)
    label.image = imgtk


def Sobel():
    global src
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    sobel_x = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    sobel_y = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])

    sobel_x = cv2.convertScaleAbs(cv2.filter2D(gray, -1, sobel_x))
    sobel_y = cv2.convertScaleAbs(cv2.filter2D(gray, -1, sobel_y))

    sobel = cv2.addWeighted(sobel_x, 1, sobel_y, 1, 0)

    fin_img = Image.fromarray(sobel)
    imgtk = ImageTk.PhotoImage(image=fin_img)
    label.config(image=imgtk)
    label.image = imgtk


def LoG():
    global src

    blur = cv2.GaussianBlur(src, (7, 7), 0)
    laplacian = cv2.Laplacian(blur, cv2.CV_64F)
    laplacian1 = laplacian/laplacian.max()

    fin_img = Image.fromarray(laplacian1)
    imgtk = ImageTk.PhotoImage(image=fin_img)
    label.config(image=imgtk)
    label.image = imgtk


def Canny():
    global src
    edge1 = cv2.Canny(src, 50, 200)
    edge2 = cv2.Canny(src, 100, 200)
    edge3 = cv2.Canny(src, 170, 200)

    fin_img = Image.fromarray(edge1)
    imgtk = ImageTk.PhotoImage(image=fin_img)
    label.config(image=imgtk)
    label.image = imgtk


window = tkinter.Tk()

window.title("MINI PHOTOSHOP")
window.geometry("640x480+100+100")

#src = cv2.imread("Lena_noise.png")

path = filedialog.askopenfilename()
if len(path) > 0:
    src = cv2.imread(path)
    src = cv2.resize(src, (640, 400))
    img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

#img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

img = Image.fromarray(img)
imgtk = ImageTk.PhotoImage(image=img)

label = tkinter.Label(window, image=imgtk)
label.place(x=80, y=60)

he = Button(window, width=20, text='Histogram Equalization',
            overrelief="solid", command=histogram_equal)
he.place(x=0, y=0)

negative = Button(window, width=20, text='Negative',
                  overrelief="solid", command=nega)
negative.place(x=150, y=0)

pow_law_transform = Button(
    window, width=20, text='Power law transformation', overrelief="solid", command=pow_law)
pow_law_transform.place(x=300, y=0)


# filter
gaussian = Button(window, width=20, text='Gaussian',
                  overrelief="solid", command=gaus)
gaussian.place(x=450, y=0)

median = Button(window, width=20, text='Median',
                overrelief="solid", command=medi)
median.place(x=600, y=0)

average = Button(window, width=20, text='Average',
                 overrelief="solid", command=aver)
average.place(x=750, y=0)

robert = Button(window, width=20, text='HighBoost',
                overrelief="solid", command=Robert)
robert.place(x=0, y=40)

prewitt = Button(window, width=20, text='Prewitt',
                 overrelief="solid", command=Prewitt)
prewitt.place(x=150, y=40)

sobel = Button(window, width=20, text='Sobel',
               overrelief="solid", command=Sobel)
sobel.place(x=300, y=40)

log = Button(window, width=20, text='LoG', overrelief="solid", command=LoG)
log.place(x=450, y=40)

canny = Button(window, width=20, text='Canny',
               overrelief="solid", command=Canny)
canny.place(x=600, y=40)


window.mainloop()
