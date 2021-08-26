#!/usr/bin/env python

import pyautogui as pg
import time
import cv2
from PIL import Image 
import pyocr
import subprocess

pyocr.tesseract.TESSERACT_CMD = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
tools = pyocr.get_available_tools()
tool = tools[0]

def click_word(word):
    sc = pg.screenshot() #始点x,y、幅、高さ
    sc.save('./eng.png')

    lang = 'eng'
    img_path = './{}.png'.format(lang)
    img = Image.open(img_path)
    out_path = './{}_{}.png'

    word_boxes = tool.image_to_string(
        img,
        lang=lang,
        builder=pyocr.builders.WordBoxBuilder(tesseract_layout=6)
    )

    out = cv2.imread(img_path)
    found = False

    for d in word_boxes:
        print(d.content)
        print(d.position)
        cv2.rectangle(out, d.position[0], d.position[1], (0, 0, 255), 2) #d.position[0]は認識した文字の左上の座標,[1]は右下
        cv2.imwrite(out_path.format(lang, 'word_boxes'), out)
        x1,y1 = d.position[0]
        x2,y2 = d.position[1]  
        if(d.content == word): #Anacondaのアイコンを認識したらクリックする
            x3 = (x1+x2)/2
            y3 = (y1+y2)/2
            pg.click(x3,y3)
            found = True

    if(found==False):
        print("Not found")


if __name__ == "__main__":
    # command = '"C:\\program files\\gimp 2\\bin\\gimp-2.10" -n '
    # subprocess.run(command, shell=True)
    # time.sleep(10)
    time.sleep(3)
    click_word("Python")
    click_word("Makelmage")
