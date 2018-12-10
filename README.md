# TinyUAV
### CAP5415- Computer Vision

A modification of the YOLO (You Only Look Once) algorithm for the detection of small unmanned aerial vehicles (UAVs) in images. This version uses modified weights in order to recognize UAVs.


### Prerequisites

Follow the instructions on the corresponding sites for installation instructions.
* Tensorflow: https://www.tensorflow.org/install/
* Keras: https://keras.io/#installation
* OpenCV: https://pypi.org/project/opencv-python/

* keras-metrics: https://github.com/netrack/keras-metrics

### Dataset preprocessing

1- Download the dataset from https://engineering.purdue.edu/~bouman/UAV_Dataset/ (both videos and annotations)

2- Assuming the videos are located at path\datasets\Videos, copy V2F.py to path\datasets\Videos and then run the script to convert the videos into image frames (output images should appear in the directory as jpg files). 

3- Assuming the frames were kept at path\datasets\Videos and the annotations were kept at path\datasets\Video_Annotation, copy convertAnnotations.py to path\datasets\Video_Annotation then modify convertAnnotations.py line 15 to the actual path of the image frames. 
```
line 15    ... "path\datasets\Video_Annotation\Clip_%d_frame%d.jpg" %(ClipIndx,L))    #Change to where you put the image frames but make sure you keep "\Clip_%d_frame%d.jpg"
```
As suggested in the comment, keep Clip_%d_frame%d.jpg" %(ClipIndx,L) as it is so that the annotations match with the corresponding frames.

4- Run the convertAnnotations.py script. A new .txt file called train.txt should be created.

5- Copy and replace the train.txt into the ...\CAP5415-TinyUAV repository (A train.txt was kept there for reference only and should be replaced with this new one)

### Training
1- Download pretrained weights at https://pjreddie.com/darknet/yolo/.

2- Put the .weights file downloaded into ...\CAP5415-TinyUAV

3- Run the convert.py to convert .weights file into .h5

4- Simply modify train.py for hyperparameters, then run train.py script to begin training.


### Testing 

Pending
Explain how to run the automated tests for this system


## Languages Used

* Python


## Credits

* Github user pjreddie for the original YOLOv3 
* Github user qqwweee for baseline keras YOLO model (https://github.com/qqwweee/keras-yolo3)



## Authors

* **Abdul Aziz Santarisi** - *Contribution*
* **Eugene Lucino** - *Contribution*
* **William Zhang** - *Contribution*
