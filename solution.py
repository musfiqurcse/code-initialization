import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def close_window():
    cv.destroyAllWindows()
    cv.waitKey(1)


if __name__ == "__main__":
    print('Give the path of Image: \n')
    path_of_file = input()
    # Read an image file using OpenCV
    img_inp = cv.imread(path_of_file)
    #If we want to read the image in gray scale mode use the following command
    #cv.imread(path_of_file, cv.IMREAD_GRAYSCALE)

    #Converting colored image to grey scale
    gray_img = cv.cvtColor(img_inp, cv.COLOR_BGR2GRAY)
    while True:
        print("""
        Instruction:
        Show Main & Greyscale Image **ENTER 1**
        Dynamically Change Thresohlding **ENTER 2**
        Exit the Instruction Process **ENTER 0**
        """)
        close_window()
        close_window()
        inp_ins = int(input())
        try:
            if inp_ins == 1:
                #Displaying the Main and Grayscale Image
                cv.imshow('Main Image', img_inp)
                cv.imshow('Gray Scale Image', gray_img)
                cv.waitKey(0)
                close_window()
            elif inp_ins == 2:
                #Applying Binary Thresholding
                print('Please enter Binary Thresholding value')
                thres_value = int(input())
                ret, thres = cv.threshold(gray_img,thres_value,255,cv.THRESH_BINARY)
                cv.imshow('Binary Image',thres)
                cv.waitKey(0)
                close_window()
            elif inp_ins == 0:
                break
        except Exception as ex:
            print('Error Occurred')
            print(ex)
    print('Application is closing')