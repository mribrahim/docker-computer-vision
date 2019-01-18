# docker-computer-vision

You can find many of libraries to develop a computer vision application.

*Usage:*

**docker run -it mribrahim/docker-computer-vision**

 *Installed libraries:* 
- python
- opencv
- dlib
- skimage
- sklearn
- tensorflow
- keras
- ..


add **-v /d/docker/examples:/home** command to share __host folder:__ *D:\docker\examples* with __container folder:__ */home*

**docker run -v /d/docker/examples:/home -it mribrahim/vision bash**
![commands to run landmarks.py file](https://github.com/mribrahim/docker-computer-vision/blob/master/commands.PNG)

![input and processed images](https://github.com/mribrahim/docker-computer-vision/blob/master/temp.PNG)
