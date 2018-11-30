C = 1      # number of the starting video clip's annotation file
nC = 49      # number of the last video clip's annotation file

CL = 0      # UAV class label




for ClipIndx in range(C, nC+1):
    f = open('Clip_%d_gt.txt'%(ClipIndx),'r') 
    L = 1

    for line in f:
            
            edit1 = line.replace("time_layer: %d detections:" % L, "/home/wzhang/computerVision/keras-yolo3/image/Clip_%d_frame%d.jpg" %(ClipIndx,L))    #Change to where you put the image frames but make sure you keep "\Clip_%d_frame%d.jpg"
            edit2 = edit1.replace(", ", ",")
            edit3 = edit2.replace("(","")
            edit4 = edit3.replace("),",",%d " %CL)
            writefile = open("train.txt", "a")
            writefile.write(edit4)
            L = L+1


writefile.close()
f.close()
