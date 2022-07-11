<!-- Intro -->
# **MOTION_ALARM**
> **Lucas Arroyo Blanco**  
> 
> _PatoOsoPatoso_  

&nbsp;

<!-- Index -->
# Table of contents
## &nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;)&nbsp;&nbsp;[Description](#description)
## &nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;)&nbsp;&nbsp;[Requeriments](#requeriments)
## &nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;)&nbsp;&nbsp;[Modifications to be used](#modifications-to-be-used)  

&nbsp;  
&nbsp; 

<!-- Description -->
## **Description**

A simple implementation of a motion based alarm in python.

If the sensor detects movement triggers a warning on the screen (for testing purposes) after that if there is ininterrumpted movement for 5 seconds starts filming, the duration of the capture will last until 5 seconds pass without movement.

&nbsp;

<!-- Requeriments -->
## **Requeriments**

* OpenCV for python
* A camera plugged into the computer

&nbsp;  

<!-- Modifications -->
## **Modifications to be used**

If you have more than one camera and want to use an other than the default one you have to modify this in order to select that one:  
```python
cap = cv2.VideoCapture(0) # Change the '0' to the device number listed by opencv
```
&nbsp;  
&nbsp;

<!-- Bye bye -->
<img src="https://static.wikia.nocookie.net/horadeaventura/images/c/c2/CaracolRJS.png/revision/latest?cb=20140518032802&path-prefix=es" alt="drawing" style="width:100px;"/>**_bye bye_**