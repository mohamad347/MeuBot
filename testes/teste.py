'''import PIL.Image
# Adding the GUI interface
from tkinter import *


arq = open("fofoca0.jpeg","rb")
img = PIL.Image.open(arq)
#img.show()

#img = Image.open("fofoca0.jpeg")
img.save("fofoca0.png")'''
from openpyxl import load_workbook

#load excel file
workbook = load_workbook(filename="reclamacoes.xlsx")

#open workbook
sheet = workbook.active

#modify the desired cell
x = sheet["A2"]
if x != None:
    print(x)

#save the file
#workbook.save(filename="reclamacoes.xlsx")
