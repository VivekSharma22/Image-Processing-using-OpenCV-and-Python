import numpy as np
import random
import cv2

a = np.zeros((500,500,3),dtype=np.uint8)
b = np.zeros((1000,1000,3),dtype=np.uint8)
c = np.zeros((800,800,3),dtype=np.uint8)

########### creating image "viv1.jpg" and then displaying it ############ 

a[0:500,0:500]=[0,255,225]
a[100:200,100:200]=[255,0,0]
a[100:200,300:400]=[255,0,0]
a[300:350,100:150]=a[350:400,150:350]=a[300:350,350:400]=[255,0,0]

cv2.imwrite("viv1.jpg",a)

viv1 = cv2.imread("viv1.jpg")
cv2.imshow("viv1",viv1)
cv2.waitKey()
cv2.destroyAllWindows()

######## creating image "viv2.jpg" and then displaying it ##############

lis = [[0,0,255],[0,255,0],[255,0,0],[255,255,255],[255,255,0],[255,0,255],[0,255,255]]
for i in range(100):
    b[(0+10*i):(10+10*i) ,(0+10*i):(10+10*i)]=random.choice(lis)
    b[(990-10*i):(1000-10*i) , (0+10*i):(10+10*i)]=random.choice(lis)
    

cv2.imwrite("viv2.jpg",b)

viv2 = cv2.imread("viv2.jpg")
cv2.imshow("viv2",viv2)
cv2.waitKey()
cv2.destroyAllWindows()

###### creating image "viv3.jpg" and then displaying it #############

for i in range(80):
    c[0:800-i*10,0:800-i*10]=random.choice(lis)
    
cv2.imwrite("viv3.jpg",c)

viv3 = cv2.imread("viv3.jpg")
cv2.imshow("viv3",viv3)
cv2.waitKey()
cv2.destroyAllWindows()
