#โชว์ภาพชั่วคราว
import cv2
img = cv2.imread(r"image/cat.jpg")


cv2.imshow("Output",img)
cv2.waitKey(delay=5000)
cv2.destroyAllWindows()