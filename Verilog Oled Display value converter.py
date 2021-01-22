from PIL import Image
import math
import os
from tkinter.filedialog import askopenfilename
from tkinter import Tk








def dB(n):  
    return bin(n).replace("0b", "") 



def getback():
    print("Input solid colour background to ignore: ")
    Tk().withdraw() 
    ignoreback = askopenfilename()
    im = Image.open(r"%s" %ignoreback)
    pixels = list(im.getdata())
    colour = ['','','']
    for j in range(3):
        if (j == 0) or (j == 2):
            colour[j] = dB(int(math.floor((pixels[0][j]/255 * 31))))
            if (len(colour[j]) < 5):
                missing = 5 - len(colour[j])
                for i in range(missing):
                    colour[j] = "0" + colour[j]
        elif (j == 1):
            colour[j] = dB(int(math.floor((pixels[0][j]/255 * 63))))
            if (len(colour[j]) < 6):
                missing = 6 - len(colour[j])
                for i in range(missing):
                    colour[j] = "0" + colour[j]

    return str(colour[0]) + str(colour[1])+  str(colour[2])







def photoconvert(n):
    filename = "image" + str(n) + ".txt"
    f = open(filename, "w")

    path = os.getcwd()

    

    ##imageinput = input ("Input image %i location: "% n)
    print("Input image %i location: "% n)
    Tk().withdraw() 
    imageinput = askopenfilename()
    

    print("Converted photo will be output as %s at %s"%(filename,path))



    im = Image.open(r"%s" %imageinput)

    




    pixels = list(im.getdata())

    outputarray = ['' for i in range(len(pixels))]
    count = 0 


    for i in range(len(pixels)):
        colour = ['','','']
        for j in range(3):
            if (j == 0) or (j == 2):
            
                colour[j] = dB(int(math.floor((pixels[i][j]/255 * 31))))

                if (len(colour[j]) < 5):
                    missing = 5 - len(colour[j])
                    for i in range(missing):
                        colour[j] = "0" + colour[j]

            
            elif (j == 1):
                colour[j] = dB(int(math.floor((pixels[i][j]/255 * 63))))
                if (len(colour[j]) < 6):
                    missing = 6 - len(colour[j])
                    for i in range(missing):
                        colour[j] = "0" + colour[j]

                    

    
        outputarray[i] = str(colour[0])+ str(colour[1])+  str(colour[2])

        if(outputarray[i] == ignore):
            count += 1
            continue

        print ( "if(my_pixel_index == %i)begin"%count, file = f)
        print ("        oled_data <= 16'b" + outputarray[i] + ";", file = f)
        print("end", file = f)

        count += 1



    f.close()

ignore = "na"
rback = input("Input Y if you want to ignore backgrounyd and select a solid colour background picutre(N otherwise): ")
if(rback == "Y" or rback == "y"):
    ignore = getback()
else:
    pass
no = input("Number of images: ")
for i in range (int(no)):
    photoconvert(i+1)

wait = input("PRESS ENTER TO CONTINUE.")

