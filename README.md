# TinyUAV
### CAP5415- Computer Vision

A modification of the YOLO (You Only Look Once) algorithm for the detection of small unmanned aerial vehicles (UAVs) in images. This version uses modified weights in order to recognize UAVs.


### Prerequisites

Follow the instructions on the following sites to install the corresponding prerequisites.
* Tensorflow: https://www.tensorflow.org/install/
* Keras: https://keras.io/#installation
* OpenCV: https://pypi.org/project/opencv-python/

* keras-metrics: https://github.com/netrack/keras-metrics

### Dataset preprocessing

1- Download the dataset from https://engineering.purdue.edu/~bouman/UAV_Dataset/ (both videos and annotations)

2- Assuming the videos are located at path\datasets\Videos, copy V2F.py to path\datasets\Videos and then run the script to convert the videos into image frames (output images should appear in the directory as jpg files). 

3- Assuming the frames were kept at path\datasets\Videos and the annotations were kept at path\datasets\Video_Annotation, copy convertAnnotations.py to path\datasets\Video_Annotation then modify convertAnnotations.py line 15 to your the actual path. 
```
line 15    ... "path\datasets\Video_Annotation\Clip_%d_frame%d.jpg" %(ClipIndx,L))    #Change to where you put the image frames but make sure you keep "\Clip_%d_frame%d.jpg"
```
As suggested in the comment, keep Clip_%d_frame%d.jpg" %(ClipIndx,L) as it is so that the annotations match with the corresponding frames.

4- Run the convertAnnotations.py script. A new .txt file called train.txt should be created.

5- Copy and replace the train.txt into the repository (A train.txt was kept there for reference only and should be replaced with this new one)

### Installing

How to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

### Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```


## Languages Used

* Python


## Authors

* **Abdul Aziz Santarisi** - *Contribution*
* **Eugene Lucino** - *Contribution*
* **William Zhang** - *Contribution*
