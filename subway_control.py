import cv2
from gesture_detector import GestureDetector
from gesture_map import map_gesture
import pyautogui
import time

detector = GestureDetector()
cap = cv2.VideoCapture(0)
time.sleep(2)  # Focus the game window

print("Subway Surfers hand control started. Press Q to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect fingers
    frame, fingers = detector.detect(frame)

    # Map gesture to action
    # Custom mapping for Subway Surfers
    if fingers == [0,1,0,0,0]:        # index finger
        pyautogui.press('left')
        action = "LEFT"
    elif fingers == [0,1,1,0,0]:      # index+middle
        pyautogui.press('right')
        
        action = "RIGHT"
    elif fingers == [1,1,1,1,1]:      # all fingers
        pyautogui.press('up')
        action = "JUMP"
    elif fingers == [1,0,0,0,0]:      # thumb up (or modify)
        pyautogui.press('down')
        action = "SLIDE"
    else:
        action = "STOP"

    # Show action on webcam
    cv2.putText(frame, f"Action: {action}", (10,40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    cv2.imshow("Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    