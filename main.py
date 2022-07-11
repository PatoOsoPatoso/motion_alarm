import os
import cv2
from time import time
from datetime import datetime

def getContours(frame1, frame2):
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    return contours

def startRecording(fourcc):
    now = datetime.now()

    date = now.strftime("%Y/%m/%d %H;%M;%S")

    path = "RECORDINGS/" + date.split()[0]
    filename = date.split()[1] + ".avi"

    if not os.path.exists(path):
        os.makedirs(path)
    out = cv2.VideoWriter(path + "/"  + filename, fourcc, 11.0, (1280,720))

    return out

def main():
    cap = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc('X','V','I','D')

    waiting = False
    filming = False

    while cap.isOpened():
        _, frame1 = cap.read()
        _, frame2 = cap.read()

        movement = False

        contours = getContours(frame1, frame2)

        for contour in contours:
            cv2.boundingRect(contour)

            if cv2.contourArea(contour) < 100:
                continue

            movement = True
            break

        if movement:
            end = time()
            if not waiting and not filming:
                start = time()
                waiting = True
            
            if waiting and time() - start > 5:
                waiting = False
                filming = True
                out = startRecording(fourcc)
        else:
            if waiting:
                waiting = False
            
            if filming and time() - end > 5:
                filming = False
                out.release()

        if waiting:
            cv2.putText(frame2, f"GRABANDO EN {str(5 - int(time() - start))}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 69, 0), 3)
        elif filming:
            image = cv2.resize(frame1, (1280,720))
            out.write(image)
            text = "GRABANDO"
            if not movement:
                text = f"LA GRABACION TERMINA EN {str(5 - int(time() - end))}"
            cv2.putText(frame2, text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 3)
        else:
            cv2.putText(frame2, "ESPERANDO MOVIMIENTO", (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 3)
        
        cv2.drawContours(frame2, contours, -1, (0, 255, 0), 2)

        cv2.imshow("feed", frame2)

        if cv2.waitKey(40) == 27:
            break

    cv2.destroyAllWindows()
    cap.release()
                
if __name__ == "__main__":
    main()