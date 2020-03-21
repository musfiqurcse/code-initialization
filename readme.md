# An OpenCV based sample Application

## Usage

1. Show color image in greyscale
2. Change Dynamically binary image threshold value

## Requirements
1. OpenCV
2. Numpy (optional)

## Running Guidelines

```shell
python3 solution.py

Give the path of Image:
<filepath>
 Instruction:
 Show Main & Greyscale Image **ENTER 1**
 Dynamically Change Thresohlding **ENTER 2**
 Exit the Instruction Process **ENTER 0**
```

## Technical Issues
1. Issue 1:
Conda 4.8.* have some issue to install openCV
`Solution: Downgrade to conda 4.3.*`
2. Issue 2:
Running code in conda for openCV , sometime `freeze the system (Ubuntu 18.04).`
However, It is a known issue
https://stackoverflow.com/questions/22681611/opencv-cv2-destroyallwindows-doesnt-respond
(Read the second answer)
