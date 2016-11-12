import numpy as np
import cv2


def denoise(frame):
    frame = cv2.medianBlur(frame, 5)
    frame = cv2.GaussianBlur(frame, (5,5), 0)
    return frame

def get_cam_frame(cam):
    ret, img = cam.read()
    # smaller frame size - things run a lot smoother than a full screen img
    # img = cv2.resize(img, (800, 450))
    return img

ALPHA = 0.001 # change this later
cv2.ocl.setUseOpenCL(False) # fix the null assertion error...
cap = cv2.VideoCapture(0) # access the webcam
# cap = cv2.VideoCapture('nadir.mp4')

BG = cv2.cvtColor(denoise(get_cam_frame(cap)), cv2.COLOR_BGR2GRAY)

while True:
    frame = get_cam_frame(cap)

    f = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # current frame in grayscale

    BG = f * ALPHA + BG * (1 - ALPHA) # update background calc

    mask = cv2.absdiff(f.astype(np.uint8), BG.astype(np.uint8))

    ret, mask = cv2.threshold(mask.astype(np.uint8), 25, 255, cv2.THRESH_BINARY) # apply threshold to diff

    cv2.imshow('fg', mask)

    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # get the contour with the greatest area; probably subject/foreground
    max_area = -1 # keep track of this
    ci = -1
    for i in range(len(contours)):
        cnt = contours[i]
        area = cv2.contourArea(cnt)

        if area > max_area:
            max_area = area
            ci = i

    if ci != -1:
        cnt = contours[ci]

        # same
        hull = cv2.convexHull(cnt)
        cv2.drawContours(frame, [hull], 0, (0, 255, 0), 2)


    cv2.imshow('img', frame)


    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
