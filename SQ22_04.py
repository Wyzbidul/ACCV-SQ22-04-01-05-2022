#####################################################################################################################################
#	PROGRAM BY : MC IATRIDES
#	LAST UPDATE : 28-04-2022
#	TITLE : SQ22-04 - (01-05-2022)
#   SUBTITLE : Design of 2D scalar field visualization
#	REDACTED FOR : ADV COURSE ON COMPUTER VISUALIZATION
#####################################################################################################################################

##### PACKAGES ######################################################################################################################
from numpy import *
import cv2 as cv
#####################################################################################################################################

###### ANALYSIS PART ################################################################################################################
print('START TESTS')

#Import original image into the program
img_A = cv.imread("pgms4sq22_04/A.pgm")
img_B = cv.imread("pgms4sq22_04/B.pgm")
height, width, _ = img_A.shape
print(height, width)

#Display the original image
cv.imshow('A', img_A)
cv.imshow('B', img_B)
cv.waitKey(0)

#Create image to use to show differences in pixel color
img_dif = img_B.copy()
img_scale = img_B.copy()
#For each pixel that is different we paint the output pixel white
for i in range(height):
    for j in range(width):
        if img_A[i,j][0] != img_B[i,j][0]:
            img_dif[i,j] = [255, 255, 255]
            dst = int(img_A[i,j][0]) - int(img_B[i,j][0])
            if dst > 0:
                img_scale[i,j] = [0, 0, 255]    #BGR => red
            else:
                img_scale[i,j] = [255, 0, 0]    #BGR => blue

#Display the resulting image
cv.imwrite('output_dif.jpg',img_dif)
cv.imshow('output_dif',img_dif)
cv.imwrite('output_scale.jpg',img_scale)
cv.imshow('output_scale',img_scale)

CLASSES = ["Lighter", "Darker"]
COLORS = [[255,0,0],[0,0,255]]
# initialize the legend visualization
legend = zeros(((len(CLASSES) * 25) + 25, 300, 3), dtype="uint8")
# loop over the class names + colors
for (i, (className, color)) in enumerate(zip(CLASSES, COLORS)):
    print(i, className, color)

cv.waitKey(0)
cv.destroyAllWindows()

print('END TESTS')
#####################################################################################################################################
