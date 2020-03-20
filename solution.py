import numpy as np
import cv2
import matplotlib.pyplot as plt
print('Give the path of Image: \n')
path_of_file = input()
image_input = cv2.imread(path_of_file)
try:
    # Image path: /home/musfiq/Public/codebase/assets/test.jpeg
    print
    cv2.imshow("Preview", image_input)
except Exception as ex:
    print(ex)
    print('File Not Found')
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
print('it is working')
