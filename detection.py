import cv2
import mediapipe as mp
import math
import time

mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True
)

LEFT_EYE = [362, 385, 387, 263, 373, 380]

def distance(p1, p2):
    return math.sqrt(
        (p1.x - p2.x)**2 +
        (p1.y - p2.y)**2
    )

def calculate_EAR(landmarks, eye_points):
    p1 = landmarks[eye_points[0]]
    p2 = landmarks[eye_points[1]]
    p3 = landmarks[eye_points[2]]
    p4 = landmarks[eye_points[3]]
    p5 = landmarks[eye_points[4]]
    p6 = landmarks[eye_points[5]]

    ear = (distance(p2,p6) + distance(p3,p5)) / (2 * distance(p1,p4))
    return ear


EAR_THRESHOLD = 0.20
closed_time = None

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:

        face = results.multi_face_landmarks[0]

        ear = calculate_EAR(face.landmark, LEFT_EYE)

        cv2.putText(
            frame,
            f"EAR: {ear:.3f}",
            (20,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )

        if ear < EAR_THRESHOLD:
            if closed_time is None:
                closed_time = time.time()

            elapsed = time.time() - closed_time

            if elapsed > 2:
                cv2.putText(
                    frame,
                    "FATIGUE DETECTED",
                    (20,90),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,0,255),
                    2
                )

        else:
            closed_time = None


    cv2.imshow("Fatigue Test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()