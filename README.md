# HandMouse
CalHacks 3.0
Using OpenCV, we created a gesture-controlled mouse which detects hand movements and positions. 
Aditionally, we created a rock, paper,scissors game which regonizes the gestures used in the traditional game. 


Requires Python 2.7.11, OpenCV 3.10, win32api for Python, numpy.
To use, just run:
        python test.py

Adjust threshold brightness: plus and minus on the num pad. 
Toggle using hand as mouse: "R"
Exit the program: ESC


To run the rock, paper, scissors demo, run:
        python rps.py

Calibrate the threshold brightness so that the number of fingers detected is accurate, and so that your hand is drawn solid white in the "Threshold" window. To be detected accurately, your hand must be completely surrounded in black. (Works best if you cover your wrist with a dark sleeve or watch.)
Press ESC to play

