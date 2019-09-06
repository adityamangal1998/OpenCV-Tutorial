import time as t

import cv2
import pyttsx3

voiceEngine = pyttsx3.init()
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

# iniciate id counter
id = 0

# names related to ids: example ==> Marcelo: id=1,  etc
names = ['None', 'Akshay', 'Mangal', 'Kajal', 'Vicky', 'Shiv']

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # set video widht
cam.set(4, 480)  # set video height

# Define min window size to be recognized as a face
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)
count = 0
while True:

    ret, img = cam.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )
    for (x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

        # Check if confidence is less them 100 ==> "0" is perfect match 
        if (confidence < 100):
            count += 1
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
            if count > 18:
                count = 0
                present_time = t.ctime()
                time = int(present_time[11:13])
                if 17 >= time >= 12:
                    mytext = "Good Afternoon "
                elif 20 >= time > 17:
                    mytext = "Good Evening "
                elif 23 >= time > 17 or 4 > time >= 0:
                    mytext = "Good Night "
                elif 12 > time >= 4:
                    mytext = "Good Morning "
                mytext = mytext + id
                voiceEngine.say(mytext)
                voiceEngine.runAndWait()
        else:
            count = 0
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))

        cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 0, 0), 2)
        cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)
        cv2.putText(img, "Press Esc for EXIT", (0, 20), font, 1, (0, 0, 255), 2)

    cv2.imshow('camera', img)

    k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
    if k == 27:
        break

print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
