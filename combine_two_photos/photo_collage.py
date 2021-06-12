import numpy,cv2
p1 = cv2.imread("p1.jpg")
p2 = cv2.imread("p2.jpg")

######## Creating a vertical collage of the two photos ############

photo = numpy.zeros(( p1.shape[0]+p2.shape[0] ,p1.shape[1], 3),dtype=numpy.uint8)

photo[0:p1.shape[0],:]=p1
photo[p1.shape[0]: , :p2.shape[1]]=p2

cv2.imshow("p1",photo)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imwrite("photo.jpg",photo)

########## Creating the Horizontal photo Collage of the two photos and displying it ##################

photo1 = numpy.zeros(( p1.shape[0] ,p1.shape[1]+p2.shape[1], 3),dtype=numpy.uint8)

photo1[:,0:p1.shape[1]]=p1
photo1[:,p1.shape[1]:] = cv2.resize(p2,(p2.shape[1],photo1.shape[0]))

cv2.imshow("p1",photo1)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imwrite("photo1.jpg",photo1)
