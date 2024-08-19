import sys

import imageio.v3 as iio
import ipympl
import matplotlib.pyplot as plt
import numpy as np
import skimage as ski
import math
import os


def toImg(text : str):
    text = bytearray(text, "utf-8")
    img = list()
    size = math.ceil(math.sqrt(math.ceil(len(text) / 3)))
    count = 0
    l = list()
    for i in text:
        l.append(i)
    print(l)
    for i in range(size):
        img.append(list())
    for i in img:
        for j in range(size):
            i.append([0, 0, 0])
    index = 0
    colorIndex = 0
    x = 0
    y = 0
    for i in img:
        for j in i:
            for k in j:
                if index >= len(text):
                    break
                img[x][y][colorIndex] = text[index]
                index += 1
                colorIndex += 1
                if colorIndex == 3:
                    colorIndex = 0
            y += 1
            if y == size:
                y = 0
        x += 1
    return img
def toText(img : list):
    oneDim = list()
    for i in img:
        for j in i:
            for k in j:
                oneDim.append(k)
    bytes = bytearray()
    for i in oneDim:
        bytes.append(i)
    while bytes.count(0):
        bytes.remove(0)
    decoden = bytes.decode("utf-8")
    return decoden

while True:
    mode = input("What do you want to do?\n1 - code text into the image\n 2 - decode text from the image\n")
    if mode == '1':
        text = ''
        modeSet = False
        while not modeSet:
            mode = input("Do you want get text from file or write it here?\n1 - write here\n2 - from file\n")
            if mode == '1' or mode == '2':
                modeSet = True
            else:
                print("Wrong input")
        if mode == '1':
            text = input("Write the text: ")
        else:
            path = input("Write the path of text file: ")
            encoding = input("Encoding of the file(press enter, if it's not important): ")
            file = 0
            if encoding == '':
                file = open(path, 'r')
            else:
                file = open(path, 'r', encoding=encoding)
            text = file.read()
            file.close()
        img = toImg(text)
        notExit = True
        fig, ax = plt.subplots()
        ax.imshow(img)
        while notExit:
            action = input("What do you want to do with image?\n1 - show image now\n2 - show text now\n3 - save it into the file\n4 - exit\n")
            if action == '1':
                plt.show()
            elif action == '2':
                print(text)
            elif action == '3':
                path = input("Write the path, where you want to save it: ")
                if not os.path.isfile(path):
                    os.mkdir(path)
                iio.imwrite(path, img)
            elif action == '4':
                notExit = False
            else:
                print("Wrong input")
    elif mode == '2':
        path = input("Write the path, where this file: ")
        img = iio.imread(path)
        text = toText(img)
        notExit = True
        while notExit:
            action = input("What do you want to do?\n1 - show image now\n2 - show text now\n3 - save text in the file\n4 - exit\n")
            if action == '1':
                fig, ax = plt.subplots()
                plt.show()
            elif action == '2':
                print(text)
            elif action == '3':
                path = input("Write the path, where you want to save it: ")
                if not os.path.isfile(path):
                    os.mkdir(path)
                file = open(path, 'w')
                file.write(text)
            elif action == '4':
                notExit = False
            else:
                print("Wrong input")
    else:
        print("Wrong input")
