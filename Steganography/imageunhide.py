from LSBSteg import LSBSteg
import cv2.cv as cv
import sys
    
inp = cv.LoadImage("resultindex.png")
steg = LSBSteg(inp)
dec = steg.unhideImage()
cv.SaveImage("recovered.png", dec) #Image retrieve into the other image

