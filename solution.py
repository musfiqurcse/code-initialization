import numpy as np
import cv2
import matplotlib.pyplot as plt
print('Give the path of Image: \n')
path_of_file = input()
image_input = cv2.imread(path_of_file)
# try:
#     # Image path: /home/musfiq/Public/codebase/assets/test.jpeg
#     print
#     cv2.imshow("Preview", image_input)
# except Exception as ex:
#     print(ex)
#     print('File Not Found')
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)
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
    """)
    input_inst = int(input())
    if input_inst == 1:
        grey_scale_image = cv2.cvtColor(image_input, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Main Image', image_input)
        cv2.imshow('Grey Scale Image', grey_scale_image)
        cv2.waitKey(0)
    elif input_inst == 0:
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        break
print('it is working')
