import math
import time
import keyboard
import cv2
import mediapipe as mp
from Functions import cursor

click_stat = 0
distance = 0
home = [0, 0]
start_track = 0
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
with mp_hands.Hands(
        min_detection_confidence=0.4,
        min_tracking_confidence=0.4) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

        image.flags.writeable = False
        results = hands.process(image)
        image_height, image_width, _ = image.shape
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for ids, landmrk in enumerate(hand_landmarks.landmark):
                    cx, cy = landmrk.x * image_width, landmrk.y * image_height
                    if ids == 8:
                        indexfingerx, indexfingery = cx, cy
                    if ids == 4:
                        thumbfingerx, thumbfingery = cx, cy
                    if ids == 0:
                        wristx, wristy = cx, cy
                    if ids == 20:
                        pinkyx, pinkyy = cx, cy
                ix = int(indexfingerx)
                iy = int(indexfingery)
                tx = int(thumbfingerx)
                ty = int(thumbfingery)
                wx = int(wristx)
                wy = int(wristy)
                px = int(pinkyx)
                py = int(pinkyy)
                try:
                    distance = math.sqrt(((ix - tx) ^ 2) - ((iy - ty) ^ 2))
                    distance_scroll = math.sqrt(((px - tx) ^ 2) - ((py - ty) ^ 2))
                except:
                    pass
                cursor(wx, wy, distance, home, distance_scroll)
                if start_track == 0 and home == [0, 0]:
                    home = [ix, iy]
                    print(home)
                start_track = 1
                print(distance)
            mp_drawing.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        else:
            start_track = 0
        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()
