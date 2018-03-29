from LSBSteg import LSBSteg
import cv2.cv as cv
import sys  

im = cv.LoadImage("res.png")
steg = LSBSteg(im)
print "Text value:",steg.unhideText()
