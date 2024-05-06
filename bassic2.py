import cv2
img = cv2.imread(r"C:\Users\teerathap\Downloads\python-opencv-main\python-opencv-main\image\cat.jpg")


cv2.imshow("Output",img)
cv2.waitKey(delay=5000)
cv2.destroyAllWindows()