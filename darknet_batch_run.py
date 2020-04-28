import os
import time

path = '<darknet_dir>'
input_path =  path + "out/"
output_path = path + "res/"
darknet = path + "darknet/"


folders = []

# r=root, d=directories, f = files
for r, d, f in os.walk(input_path):
    for folder in d:
        folders.append(os.path.join(r, folder))
    folders.append(f)
    # print(f)

for f in range(0,len(folders[0])):
    print(folders[0][f])
    os.system(darknet+ "darknet detector test cfg/voc.data cfg/voc.cfg weights/voc.weights "+input_path+folders[0][f])
    os.system("scp "+darknet+"/predictions.jpg "+output_path+"output_"+folders[0][f])
    print('=======CPU RESTING FOR 10 Seconds ========')
    time.sleep(10)
