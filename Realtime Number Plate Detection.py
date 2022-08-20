# For real time number plate detection we use open cv Haar feature-based classifiers in this project.

import cv2

frameWidth = 640
frameHeight = 480
# Create a trained classifier object with the xml file
nPlateCascade = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")
minArea = 250
color = (255,0,255)

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(12,150)
count = 0

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply OpenCV’s detectMultiScale() function to detect the number /license plates.
    VehiclenumberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 10)

# Once the detection is done, the result is a list of bounding boxes (x, y, w, h) representing the
    # location of each plate the classifier found.
    for (x, y, w, h) in  VehiclenumberPlates:
        area = w*h
# Draw Rectanle around the detected image
        if area >minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.putText(img," Vehicle number Plate",(x,y-5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
# Extract region of intrest
            imgRoi = img[y:y+h,x:x+w]
            cv2.imshow("ROI", imgRoi)

    cv2.imshow("Detecting", img)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("Resources/Scanned/ no Vehicle numberPlate"+str(count)+".jpg",imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,
                    2,(0,0,255),2)
        cv2.imshow(" Vehicle number Plate Detection",img)
        cv2.waitKey(500)
        count +=1