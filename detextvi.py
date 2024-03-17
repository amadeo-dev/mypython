import cv2
import os
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #
specs_ori = cv2.imread('glass.png', -1)

def transparentOverlay(src, overlay, pos=(0, 0), scale=1):
    overlay = cv2.resize(overlay, (0, 0), fx=scale, fy=scale)
    h, w, _ = overlay.shape  # Size of foreground
    rows, cols, _ = src.shape  # Size of background Image
    y, x = pos[0], pos[1]  # Position of foreground/overlay image

    for i in range(h):
        for j in range(w):
            if x + i >= rows or y + j >= cols:
                continue
            alpha = float(overlay[i][j][3] / 255.0)  # read the alpha channel
            src[x + i][y + j] = alpha * overlay[i][j][:3] + (1 - alpha) * src[x + i][y + j]
    return src

def detect(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for(x, y, w, h) in faces:
        glass_symin = int(y + 1.5 * h / 5)
        glass_symax = int(y + 2.5 * h / 5)
        sh_glass = glass_symax - glass_symin
        #cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 7)

        face_glass_roi_color = img[glass_symin:glass_symax, x:x + w]
       
        specs = cv2.resize(specs_ori, (w, sh_glass), interpolation=cv2.INTER_CUBIC)
       
        transparentOverlay(face_glass_roi_color, specs)



def compute_webcam():
    cap = cv2.VideoCapture(0)
    while 1:
        ret, img = cap.read()
        #cv2.imshow('img', img)
        detect(img)
        cv2.imshow('image',img )
        key = cv2.waitKey(1)
        if key == 27:
            break
           
compute_webcam()