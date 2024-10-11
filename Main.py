import math
import time
import keyboard
import cv2
import mediapipe as mp
from Functions import cursor, click, scroll

global image_height, image_width
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    min_detection_confidence = 0.4,
    min_tracking_confidence = 0.4) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty cam")
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
                    if ids == 8:
                        ix, iy = int(landmrk.x * image_width), int(landmrk.y * image_height)
                    if ids == 4:
                        tx, ty = int(landmrk.x * image_width), int(landmrk.y * image_height)
                    if ids == 0:
                        wx, wy = int(landmrk.x * image_width), int(landmrk.y * image_height)
                    if ids == 20:
                        mx, my = int(landmrk.x * image_width), int(landmrk.y * image_height)
                try:
                    dist_i_t = math.sqrt(((ix - tx) ^ 2) - ((iy - ty) ^ 2))
                    dist_m_t = math.sqrt(((mx - tx) ^ 2) - ((my - ty) ^ 2))
                except:
                    print("Math Error")

                # Function Placeholder
                try:
                    cursor(wx, wy, image_width, image_height)
                    click(dist_i_t)
                    #scroll(dist_m_t)
                    print(dist_i_t, dist_m_t)
                except:
                    pass

            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()



