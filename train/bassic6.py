#เปิดกล้องด้วย openCV เเละกดหยุดด้วยปุ่ม E
import cv2

cap = cv2.VideoCapture(0)

while(True):
    check , frame = cap.read()
    cv2.imshow("",frame)

    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

cap.release()
cv2.destroyAllWindows()