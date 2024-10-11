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

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
        min_detection_confidence=0.4,
        min_tracking_confidence=0.4) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # Flip the image horizontally for a later selfie-view display, and convert
        # the BGR image to RGB.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        results = hands.process(image)
        image_height, image_width, _ = image.shape
        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Here is How to Get All the Coordinates
                for ids, landmrk in enumerate(hand_landmarks.landmark):
                    # print(ids, landmrk)
                    cx, cy = landmrk.x * image_width, landmrk.y * image_height
                    if ids == 8:
                        indexfingerx, indexfingery = cx, cy
                    if ids == 4:
                        thumbfingerx, thumbfingery = cx, cy
                    if ids == 0:
                        wristx, wristy = cx, cy
                    if ids == 20:
                        pinkyx, pinkyy = cx, cy
                    # print (ids, cx, cy)
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
                    # print(distance_scroll)
                except:
                    pass

                # click_previous = click_stat
                # click_stat = 0
                # if distance < 4 and click_stat == 0:
                #     click_stat = 1
                #     keyboard.press_and_release('space')
                # if click_previous != click_stat:
                #     time.sleep(1)
                # print(click_stat)
                # print(distance)
                # print(f'Index: {landmrkindex}, Thumb: {landmrkthumb}')
                # click(distance, click_stat)
                #cursor(wx, wy, distance, home, distance_scroll)
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
