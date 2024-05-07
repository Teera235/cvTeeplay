import cv2
import mediapipe as mp

mpHands = mp.solutions.hands
Hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

image_to_overlay = cv2.imread('Tee.png') 


desired_width = 150
desired_height = 79

image_to_overlay_resized = cv2.resize(image_to_overlay, (desired_width, desired_height))

while (cap.isOpened()):
    success, img = cap.read()
    converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Hands.process(converted_image)

    if results.multi_hand_landmarks:
        for hand_in_frame in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, hand_in_frame, mpHands.HAND_CONNECTIONS)

            for id, lm in enumerate(hand_in_frame.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                if id == 8:  
                    
                    overlay_x = cx - desired_width // 2
                    overlay_y = cy - desired_height // 2

                    overlay_x = max(0, overlay_x)
                    overlay_y = max(0, overlay_y)

                    overlay_width = min(desired_width, w - overlay_x)
                    overlay_height = min(desired_height, h - overlay_y)

                    img[overlay_y:overlay_y + overlay_height, overlay_x:overlay_x + overlay_width] = \
                        image_to_overlay_resized[:overlay_height, :overlay_width]

    cv2.imshow("", img)

    if cv2.waitKey(1) == 113:
        break

cap.release()
cv2.destroyAllWindows()
