C = 1      # number of the starting video clip's annotation file
nC = 50      # number of the last video clip's annotation file

CL = 0      # UAV class label




for ClipIndx in range(C, nC+1):
    f = open('Clip_%d_gt.txt'%(ClipIndx),'r') 
    L = 1

    for line in f:
            
            edit1 = line.replace("time_layer: %d detections:" % L, "path\datasets\Video_Annotation\Clip_%d_frame%d.jpg" %(ClipIndx,L))    #Change to where you put the image frames but make sure you keep "\Clip_%d_frame%d.jpg"
            edit2 = edit1.replace(", ", ",")
            edit3 = edit2.replace("(","")
            edit4 = edit3.replace("),",",%d " %CL)
            edit5 = [x.strip() for x in edit4.split()]
            if len(edit5) > 1:
                edit7 = edit5[0]
                for i in range(1, len(edit5)):
                    edit6 = [x.strip() for x in edit5[i].split(',')]
                    edit7 = edit7+" "+edit6[1]+","+edit6[0]+","+edit6[3]+","+edit6[2]+","+edit6[4]
                writefile = open("train.txt", "a")
                writefile.write(edit7+"\n")
            else:
                writefile = open("train.txt", "a")
                writefile.write(edit5[0]+"\n")
                print(edit5[0]+"\n")

            L = L+1


writefile.close()
f.close()