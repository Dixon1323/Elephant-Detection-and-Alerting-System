import cv2
import time
import requests
import serial

first_frame = None

# ser = serial.Serial('/dev/cu.usbserial-1410', 115200)
video = cv2.VideoCapture("video.mp4")

while True:
    check, frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame=gray
        continue

    delta_frame=cv2.absdiff(first_frame,gray)
    thresh_frame=cv2.threshold(delta_frame, 35, 255, cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)

    (cnts,_)=cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 35:
            continue

        (x, y, w, h)=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)
        print("Elephant detected")
        b="2"
        # ser.write(b.encode())
        requests.get("https://blynk.cloud/external/api/update?token=GVSPp5gNZld23s9eHSZpL-FUf472F-Y6&v0=50")
        time.sleep(0.2)
        val=requests.get("https://blynk.cloud/external/api/update?token=GVSPp5gNZld23s9eHSZpL-FUf472F-Y6&v0=0")

 


    cv2.imshow("Gray Frame",gray)
    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Threshold Frame",thresh_frame)
    cv2.imshow("Color Frame",frame)

    key=cv2.waitKey(1)

    if key == ord('q'):
        break

    time.sleep(0.3)



video.release()
cv2.destroyAllWindows