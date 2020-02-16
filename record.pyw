import cv2
import numpy as np
import pyautogui as pag
from datetime import datetime

SCREEN_SIZE = (2560, 1440)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
title = datetime.now().strftime('%Y-%m-%d %H%M%S') + ".avi"
#title = 'aaa.avi'
out = cv2.VideoWriter('./'+ title, fourcc, 20.0, (SCREEN_SIZE))

# Ctrl + G
while True:
    img = pag.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    ss = cv2.resize(frame, dsize=(0, 0), fx=0.1, fy=0.1, interpolation=cv2.INTER_LINEAR)
    cv2.imshow("screenshot", ss)
    if cv2.waitKey(1) == 7:
        break

cv2.destroyAllWindows()
out.release()
