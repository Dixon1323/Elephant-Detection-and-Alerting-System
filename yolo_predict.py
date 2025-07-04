from ultralytics import YOLO
import cv2
import math 
import time
import serial
import requests

ser = serial.Serial('/dev/cu.usbserial-1410', 115200)


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


model = YOLO("yolov8x.pt")


classNames = model.names


while True:
    success, img = cap.read()
    results = model(img, stream=True)


    for r in results:
        boxes = r.boxes

        for box in boxes:

            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) 

            

            
            confidence = math.ceil((box.conf[0]*100))/100
            print("Confidence --->",confidence)

            
            cls = int(box.cls[0])
            print("Class name -->", classNames[cls])
            a=classNames[cls]
            # print(a)

            
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2
            if(a=="elephant"):
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                print(x1," ",y1," ",x2," ",y2)
                cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)
                b="2"
                ser.write(b.encode())
                requests.get("https://blynk.cloud/external/api/update?token=YOUR_BLYNK_AUTH_KEY&v0=50")
                time.sleep(0.2)
                val=requests.get("https://blynk.cloud/external/api/update?token=YOUR_BLYNK_AUTH_KEY&v0=0")


    cv2.imshow('Webcam', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()