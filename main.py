from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import cv2 as cv
from PIL import Image, ImageTk
import numpy as np

global img
global img_name


def minimum_filter(image):
    kernel = np.ones((3, 3), np.uint8)
    image = cv.erode(image, kernel)
    return image


def maximum_filter(image):
    kernel = np.ones((3, 3), np.uint8)
    image = cv.dilate(image, kernel)
    return image


def median_filter(image):
    image = cv.medianBlur(image, 5)
    return image


def otsu_gray_filter(image):
    ret, th = cv.threshold(image, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    return th


def otsu_rgb_filter(image):
    b, g, r = cv.split(image)

    ret1, th1 = cv.threshold(r, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    ret2, th2 = cv.threshold(g, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    ret3, th3 = cv.threshold(b, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

    image = cv.merge((th3, th2, th1))
    return image


def triangle_gray_filter(image):
    ret, th = cv.threshold(image, 0, 255, cv.THRESH_BINARY + cv.THRESH_TRIANGLE)
    return th


def triangle_rgb_filter(image):
    b, g, r = cv.split(image)

    ret1, th1 = cv.threshold(r, 0, 255, cv.THRESH_BINARY + cv.THRESH_TRIANGLE)
    ret2, th2 = cv.threshold(g, 0, 255, cv.THRESH_BINARY + cv.THRESH_TRIANGLE)
    ret3, th3 = cv.threshold(b, 0, 255, cv.THRESH_BINARY + cv.THRESH_TRIANGLE)

    image = cv.merge((th3, th2, th1))
    return image


def adaptive_mean_gray_filter(image):
    image = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
    return image


def adaptive_mean_rbg_filter(image):
    b, g, r = cv.split(image)

    th1 = cv.adaptiveThreshold(r, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
    th2 = cv.adaptiveThreshold(g, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
    th3 = cv.adaptiveThreshold(b, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)

    image = cv.merge((th3, th2, th1))
    return image


def adaptive_gaussian_gray_filter(image):
    image = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
    return image


def adaptive_gaussian_rbg_filter(image):
    b, g, r = cv.split(image)

    th1 = cv.adaptiveThreshold(r, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
    th2 = cv.adaptiveThreshold(g, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
    th3 = cv.adaptiveThreshold(b, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

    image = cv.merge((th3, th2, th1))
    return image


def resize_image(image):
    max_size = [500, 500]

    if image.shape[0] > image.shape[1]:
        scale = max_size[0] / image.shape[0]
    else:
        scale = max_size[1] / image.shape[1]

    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)

    dsize = (width, height)
    return cv.resize(image, dsize)


def on_min_btn_click():
    try:
        converted_img = minimum_filter(img)
        show_image(img, True)
        show_converted_image(converted_img, True)
    except Exception as e:
        print("Error! No Image Found")


def on_max_btn_click():
    try:
        converted_img = maximum_filter(img)
        show_image(img, True)
        show_converted_image(converted_img, True)
    except Exception as e:
        print("Error! No Image Found")


def on_median_btn_click():
    try:
        converted_img = median_filter(img)
        show_image(img, True)
        show_converted_image(converted_img, True)
    except Exception as e:
        print("Error! No Image Found")


def on_otsu_gray_btn_click():
    try:
        img_gray = cv.imdecode(np.fromfile(img_name, dtype=np.uint8), cv.IMREAD_GRAYSCALE)
        converted_img = otsu_gray_filter(img_gray)
        show_image(img_gray, False)
        show_converted_image(converted_img, False)
    except Exception as e:
        print("Error! No Image Found")


def on_otsu_rgb_btn_click():
    try:
        converted_img = otsu_rgb_filter(img)
        show_image(img, True)
        show_converted_image(converted_img, True)
    except Exception as e:
        print("Error! No Image Found")


def on_triangle_gray_btn_click():
    try:
        img_gray = cv.imdecode(np.fromfile(img_name, dtype=np.uint8), cv.IMREAD_GRAYSCALE)
        converted_img = triangle_gray_filter(img_gray)
        show_image(img_gray, False)
        show_converted_image(converted_img, False)
    except Exception as e:
        print("Error! No Image Found")


def on_triangle_rgb_btn_click():
    try:
        converted_img = triangle_rgb_filter(img)
        show_image(img, True)
        show_converted_image(converted_img, True)
    except Exception as e:
        print("Error! No Image Found")


def on_adaptive_mean_gray_btn_click():
    try:
        img_gray = cv.imdecode(np.fromfile(img_name, dtype=np.uint8), cv.IMREAD_GRAYSCALE)
        converted_img = adaptive_mean_gray_filter(img_gray)
        show_image(img_gray, False)
        show_converted_image(converted_img, False)
    except Exception as e:
        print("Error! No Image Found")


def on_adaptive_mean_rgb_btn_click():
    try:
        converted_img = adaptive_mean_rbg_filter(img)
        show_image(img, True)
        show_converted_image(converted_img, True)
    except Exception as e:
        print("Error! No Image Found")


def on_adaptive_gaussian_gray_btn_click():
    try:
        img_gray = cv.imdecode(np.fromfile(img_name, dtype=np.uint8), cv.IMREAD_GRAYSCALE)
        converted_img = adaptive_gaussian_gray_filter(img_gray)
        show_image(img_gray, False)
        show_converted_image(converted_img, False)
    except Exception as e:
        print("Error! No Image Found")


def on_adaptive_gaussian_rgb_btn_click():
    try:
        converted_img = adaptive_gaussian_rbg_filter(img)
        show_image(img, True)
        show_converted_image(converted_img, True)
    except Exception as e:
        print("Error! No Image Found")


def open_file():
    global img
    global img_name
    filepath = filedialog.askopenfilename(filetypes=[("Images", "*.jpeg *.jpg *.bmp *.png *.tiff *.tif *.jfif")])
    if filepath != "":
        img_name = filepath
        img = cv.imdecode(np.fromfile(filepath, dtype=np.uint8), cv.IMREAD_COLOR)
        converted_img = img
        show_image(img, True)
        show_converted_image(converted_img, True)


def show_image(image, transfer_to_rgb):
    img_to_show = resize_image(image)
    if transfer_to_rgb:
        img_to_show = img_to_show[..., ::-1].copy()
    imgtk = ImageTk.PhotoImage(image=Image.fromarray(img_to_show))
    label_img.configure(image=imgtk)
    label_img.image = imgtk
    label_img.pack(side=LEFT, padx=25)


def show_converted_image(converted_image, transfer_to_rgb):
    converted_img_to_show = resize_image(converted_image)
    if transfer_to_rgb:
        converted_img_to_show = converted_img_to_show[..., ::-1].copy()
    imgtk = ImageTk.PhotoImage(image=Image.fromarray(converted_img_to_show))
    label_converted_img.configure(image=imgtk)
    label_converted_img.image = imgtk
    label_converted_img.pack(side=RIGHT, padx=25)


def show_buttons():
    open_file_btn = ttk.Button(text="Открыть файл", command=open_file, width=60)
    open_file_btn.pack(anchor=N)

    nonlinear_frame = Frame(root)
    nonlinear_frame.pack()
    min_btn = ttk.Button(nonlinear_frame, text="Фильтр минимума", command=on_min_btn_click, width=39)
    min_btn.grid(row=0, column=0)
    max_btn = ttk.Button(nonlinear_frame, text="Фильтр максимума", command=on_max_btn_click, width=40)
    max_btn.grid(row=0, column=1)
    median_btn = ttk.Button(nonlinear_frame, text="Медианный фильтр", command=on_median_btn_click, width=39)
    median_btn.grid(row=0, column=2)

    otsu_frame = Frame(root)
    otsu_frame.pack()
    otsu_gray_btn = ttk.Button(otsu_frame, text="Метод Отсу (GRAY)", command=on_otsu_gray_btn_click, width=60)
    otsu_gray_btn.grid(row=0, column=1)
    otsu_rgb_btn = ttk.Button(otsu_frame, text="Метод Отсу (RGB)", command=on_otsu_rgb_btn_click, width=60)
    otsu_rgb_btn.grid(row=0, column=2)

    triangle_frame = Frame(root)
    triangle_frame.pack()
    triangle_gray_btn = ttk.Button(triangle_frame,
                                   text="                      Глобальная пороговая обработка.\nВыбор порога c использованием Triangle method (GRAY)",
                                   command=on_triangle_gray_btn_click, width=60)
    triangle_gray_btn.grid(row=0, column=1)
    triangle_rgb_btn = ttk.Button(triangle_frame,
                                  text="                      Глобальная пороговая обработка.\nВыбор порога c использованием Triangle method (RGB)",
                                  command=on_triangle_rgb_btn_click, width=60)
    triangle_rgb_btn.grid(row=0, column=2)

    adaptive_mean_frame = Frame(root)
    adaptive_mean_frame.pack()
    adaptive_mean_gray_btn = ttk.Button(adaptive_mean_frame, text="Адаптивная пороговая обработка MEAN (GRAY)",
                                        command=on_adaptive_mean_gray_btn_click, width=60)
    adaptive_mean_gray_btn.grid(row=0, column=1)
    adaptive_mean_rgb_btn = ttk.Button(adaptive_mean_frame, text="Адаптивная пороговая обработка MEAN (RGB)",
                                       command=on_adaptive_mean_rgb_btn_click, width=60)
    adaptive_mean_rgb_btn.grid(row=0, column=2)

    adaptive_gaussian_frame = Frame(root)
    adaptive_gaussian_frame.pack()
    adaptive_gaussian_gray_btn = ttk.Button(adaptive_gaussian_frame,
                                            text="Адаптивная пороговая обработка GAUSSIAN (GRAY)",
                                            command=on_adaptive_gaussian_gray_btn_click, width=60)
    adaptive_gaussian_gray_btn.grid(row=0, column=1)
    adaptive_gaussian_rgb_btn = ttk.Button(adaptive_gaussian_frame,
                                           text="Адаптивная пороговая обработка GAUSSIAN (RGB)",
                                           command=on_adaptive_gaussian_rgb_btn_click, width=60)
    adaptive_gaussian_rgb_btn.grid(row=0, column=2)


root = Tk()
root.title("Lab3")
root.geometry("1100x700")

label_img = ttk.Label(root)
label_converted_img = ttk.Label(root)

show_buttons()
root.mainloop()
