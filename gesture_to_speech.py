import cv2
import mediapipe as mp
import pyttsx3

# Initialize MediaPipe, OpenCV, and TTS
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

engine = pyttsx3.init()
engine.setProperty('rate', 150)

gesture_dict = {
    "Open Palm": "Hello",
    "Peace": "Peace Sign",
    "Thumbs Up": "Thumbs up",
    "Thumbs Down": "Thumbs down",
    "Call Me": "Call me",
    "Pointing": "Pointing",
    "Rock": "Rock on",
    "Double Open Palm": "Hello with both hands",
}

# Start video capture
cap = cv2.VideoCapture(0)

spoken = ""  # To prevent repeating the same speech


def get_finger_status(landmarks):
    """Returns a list like [thumb, index, middle, ring, pinky] where 1=up, 0=down"""
    fingers = []

    # Thumb (compare x for horizontal movement)
    if landmarks[4][0] > landmarks[3][0]:  # Right hand (assuming mirrored camera)
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers (compare y for vertical movement)
    tips = [8, 12, 16, 20]
    joints = [6, 10, 14, 18]

    for tip, joint in zip(tips, joints):
        if landmarks[tip][1] < landmarks[joint][1]:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers


def detect_gesture(landmarks):
    fingers = get_finger_status(landmarks)

    if fingers == [1, 1, 1, 1, 1]:
        return "Open Palm"
    elif fingers == [0, 1, 1, 0, 0]:
        return "Peace"
    elif fingers == [1, 0, 0, 0, 0]:
        return "Thumbs Up"
    elif fingers == [0, 0, 0, 0, 1]:
        return "Thumbs Down"
    elif fingers == [1, 0, 0, 0, 1]:
        return "Call Me"
    elif fingers == [0, 1, 0, 0, 0]:
        return "Pointing"
    elif fingers == [0, 1, 0, 0, 1]:
        return "Rock"
    else:
        return "Unknown"


while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    hand_landmarks_list = []
    gesture = "None"

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Extract landmark coordinates
            landmarks = []
            for lm in hand_landmarks.landmark:
                h, w, _ = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmarks.append((cx, cy))

            hand_landmarks_list.append(landmarks)

    # Detect two-hand gestures
    if len(hand_landmarks_list) == 2:
        fingers1 = get_finger_status(hand_landmarks_list[0])
        fingers2 = get_finger_status(hand_landmarks_list[1])

        if fingers1 == [1, 1, 1, 1, 1] and fingers2 == [1, 1, 1, 1, 1]:
            gesture = "Double Open Palm"
    elif len(hand_landmarks_list) == 1:
        gesture = detect_gesture(hand_landmarks_list[0])

    # Speak and display result
    text = gesture_dict.get(gesture, "")
    if gesture != "Unknown" and text != "" and text != spoken:
        spoken = text
        engine.say(text)
        engine.runAndWait()

    cv2.putText(frame, f"Gesture: {gesture}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)

    cv2.imshow("Hand Gesture to Speech", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()