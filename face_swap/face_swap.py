import cv2
import numpy
p1 = cv2.imread("p1.jpg")
p2 = cv2.imread("p2.jpg")

model = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

f1 =  model.detectMultiScale(p1)
f2 =  model.detectMultiScale(p2)

######## extracting coordinated of faces from the output of model.detectmultiScale() function then putting rectangle aroung the faces #########

x1=f1[0][0]
y1=f1[0][1]
x2=x1 + f1[0][2]
y2=y1 + f1[0][3]

rp1 = cv2.rectangle(p1, (x1,y1),(x2,y2), [0,255,0], 5 )

xx1=f2[0][0]
yy1=f2[0][1]
xx2=xx1 + f2[0][2]
yy2=yy1 + f2[0][3]

rp2 = cv2.rectangle(p2, (xx1,yy1),(xx2,yy2), [0,255,0], 5 )

cv2.imshow("rp1",rp1)
cv2.imshow("rp2",rp2)
cv2.waitKey()
cv2.destroyAllWindows()

######### swapping the faces in the two images and then displaying the inages ############

temp = numpy.zeros((y2-y1,x2-x1,3),dtype=numpy.uint8)
temp[0:y2-y1,0:x2-x1] = p1[y1:y2,x1:x2]

p1[y1:y2,x1:x2] = cv2.resize(p2[yy1:yy2 , xx1:xx2] , (y2-y1 , x2-x1))
p2[yy1:yy2 , xx1:xx2] = cv2.resize(temp , (yy2-yy1 , xx2-xx1))

cv2.imshow("p1",p1)
cv2.imshow("p2",p2)
cv2.waitKey()
cv2.destroyAllWindows()
