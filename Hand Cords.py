import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
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
        # if results.multi_hand_landmarks:
        #   print(enumerate(results.multi_hand_landmarks))
        #   break
        for id, pos in enumerate(results.multi_hand_landmarks):
            if id == 4:
                ix = pos.x * image_width
                iy = pos.y * image_height
        print(ix, iy)
        # for landmrk in results.multi_hand_landmarks:
        #   pass
        # for hand_landmarks in results.multi_hand_landmarks:
        #   # Here is How to Get All the Coordinates
        #   # for ids, landmrk in enumerate(hand_landmarks.landmark):
        #   #     # print(ids, landmrk)
        #   #     cx, cy = landmrk.x * image_width, landmrk.y*image_height
        #   #     # print(cx, cy)
        #   #     # print (ids, cx, cy)
        #   enumerate(hand_landmarks.landmark)
        #   mp_drawing.draw_landmarks(
        #       image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        # indextipx = results.multi_hand_lanmarks.landmark
        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()
