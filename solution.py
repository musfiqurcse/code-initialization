import numpy as np
import cv2
import matplotlib.pyplot as plt
print('Give the path of Image: \n')
path_of_file = input()
image_input = cv2.imread(path_of_file)
while True:
    """
    Instruction:
    Show Only Greyscale **ENTER 1**
    Dynamically Change Thresohlding **ENTER 2**
    """
    print("""
    Instruction:
    Show Only Greyscale **ENTER 1**
    Dynamically Change Thresohlding **ENTER 2**
    Exit the Instruction Process **ENTER 0**
    """)
    input_inst = int(input())
    try:
        if input_inst == 1:
            grey_scale_image = cv2.cvtColor(image_input, cv2.COLOR_BGR2GRAY)
            cv2.imshow('Main Image', image_input)
            cv2.imshow('Grey Scale Image', grey_scale_image)
            cv2.waitKey(0)
        elif input_inst == 0:
            cv2.destroyAllWindows()
            cv2.waitKey(1)
            break
    except Exception as ex:
        print('Error Occurred')
        print(ex)
print('Application is closing')