import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector


cap = cv2.VideoCapture(0)

detector = HandDetector(maxHands=1)

while True:
    success, img = cap.read()

    hands, img =detector.findHands(img)

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        if not(fingers[0] or fingers[1] or fingers[2] or fingers[3] or fingers[4]):
            print("Rock")
        elif fingers[0] and fingers[1] and fingers[2] and fingers[3] and fingers[4]:
            print("Paper")    
        elif fingers[1] and fingers[2]:
            print("Scissors")
       
        else:
            print("No symbol")

    cv2.imshow("Image", img)
    cv2.waitKey(1)
