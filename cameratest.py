import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erreur : impossible d'ouvrir la caméra.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Erreur lors de la lecture de la caméra.")
        break

    cv2.imshow("Camera Test", frame)

    # Appuyez sur q pour quitter
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()