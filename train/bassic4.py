#ปรับสีภาพ
import cv2 
img = cv2.imread(r"image/cat.jpg", -1)
imgsize = cv2.resize(img,(400,400))

cv2.imshow("",imgsize)
cv2.waitKey(0)
cv2.destroyAllWindows()