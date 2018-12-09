C = 1       # number of starting clip to be converted to frames
nC = 50     # number of the last video clip

import cv2

for ClipIndx in range(C, nC+1):
  vidcap = cv2.VideoCapture('Clip_%d.mov' % ClipIndx) 
  success,image = vidcap.read()
  count = 1
  success = True
  while success:
   cv2.imwrite("Clip_%d_frame%d.jpg" % ( ClipIndx,count), image)        
   success,image = vidcap.read()
   print('Read a new frame: ', success)
   count += 1