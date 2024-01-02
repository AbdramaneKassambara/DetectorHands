# import les biblioteque
import cv2
from cvzone.HandTrackingModule import HandDetector  # Mettez à jour l'importation ici
# initialisation de la camera
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
#init detect
detector = HandDetector(maxHands=1,detectionCon=0.8)
while True:
    success, img = camera.read()
    # dectect la main 
    hands,img = detector.findHands(img)
    # Vérifier s'il y a des mains détectées
    if hands:
        for hand in hands:
            handType = "Droite" if hand["type"] == "Right" else "Gauche"
            text = f" Main {handType} "
            org = (50, 50)
            fontFace = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (0, 255, 0)  # Vert en BGR
            thickness = 2
            lineType = cv2.LINE_AA
            cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType)
    # Affiche de l'image avec le dectect main 
    cv2.imshow("Dectection des main",img)
    # Pour quitter la boucle lorsque la touche 'q' est pressée
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.waitKey(1)

# Libération des ressources et fermeture de la fenêtre
camera.release()
cv2.destroyAllWindows()