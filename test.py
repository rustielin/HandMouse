import cv2
import numpy as np
import math
import win32api, win32con
from mouse_commands import *
SCROLL_INVERSE_GAIN = 5
STATES = {

}


def threshold(img):
    grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    value = (35, 35)
    blurred = cv2.GaussianBlur(grey, value, 0)
    _, threshholded = cv2.threshold(blurred, 80, 255,
                               cv2.THRESH_BINARY)
    return threshholded

def extractHandContour(contours):
    maxArea, index = 0, 0
    for i in xrange(len(contours)):
        area = cv2.contourArea(contours[i])
        if area > maxArea:
            maxArea = area
            index = i
    realHandContour = contours[index]
    realHandLen = cv2.arcLength(realHandContour, True)
    handContour = cv2.approxPolyDP(realHandContour,
                                        0.001 * realHandLen, True)
    return handContour

def centerWithReduction(handContour):
        scaleFactor = 0.3
        shrunk = np.array(handContour * scaleFactor, dtype=np.int32)
        tx, ty, w, h = cv2.boundingRect(shrunk)
        maxPoint = None
        maxRadius = 0
        for x in xrange(w):
            for y in xrange(h):
                rad = cv2.pointPolygonTest(shrunk, (tx + x, ty + y), True)
                if rad > maxRadius:
                    maxPoint = (tx + x, ty + y)
                    maxRadius = rad
        try:
            realCenter = np.array(np.array(maxPoint) / scaleFactor,
                                      dtype=np.int32)
            error = int((1 / scaleFactor) * 1.5)
            maxPoint = None
            maxRadius = 0
            for x in xrange(realCenter[0] - error, realCenter[0] + error):
                for y in xrange(realCenter[1] - error, realCenter[1] + error):
                    rad = cv2.pointPolygonTest(handContour, (x, y), True)
                    if rad > maxRadius:
                        maxPoint = (x, y)
                        maxRadius = rad
        except :
            maxPoint = None

        return np.array(maxPoint)

def findCircle(handContour):
    palmCenter = centerWithReduction(handContour)
    palmRadius = cv2.pointPolygonTest(handContour, tuple(palmCenter), True)
    return palmCenter, palmRadius

def findHullAndDefects(handContour):
    hullHandContour = cv2.convexHull(handContour, returnPoints = False)
    hullPoints = [handContour[i[0]] for i in hullHandContour]
    hullPoints = np.array(hullPoints, dtype = np.int32)
    defects = cv2.convexityDefects(handContour, hullHandContour)
    return hullPoints, defects

def drawVertices(points, drawing):
    for i in xrange(len(points)):
            for j in xrange(len(points[i])):
                cv2.circle(drawing, (points[i][j][0], points[i][j][1]), 2, (255,255,255))

# def getNumFingers(points):


cap = cv2.VideoCapture(0)

while(cap.isOpened()):

    # ugliest workaround. joe: "*frown"
    try:
        ret, img = cap.read()
        cv2.rectangle(img,(300,300),(100,100),(0,255,0),0)
        crop_img = img[100:300, 100:300]
        # crop_img = img

        thresh1 = threshold(crop_img)

        cv2.imshow('Thresholded', thresh1)

        image, contours, hierarchy = cv2.findContours(thresh1.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


        handContour = extractHandContour(contours)
        palmCenter, palmRadius = findCircle(handContour)

        minX, minY, handWidth, handHeight = cv2.boundingRect(handContour)

        # palmCenter, palmRadius = findCircle(handContour)

        x = 1920 -  palmCenter[0] * 1920//200
        y = palmCenter[1] * 1080//200

        win32api.SetCursorPos((x, y))


        # find all that shit
        hullPoints, defects = findHullAndDefects(handContour)





        # cnt = max(contours, key = lambda x: cv2.contourArea(x))
        #
        # x,y,w,h = cv2.boundingRect(cnt)
        # cv2.rectangle(crop_img,(x,y),(x+w,y+h),(0,0,255),0)


        win32api.SetCursorPos((x, y))
        mouse.x, mouse.y = win32api.GetCursorPos()


        # hull = cv2.convexHull(cnt)

        drawing = np.zeros(crop_img.shape,np.uint8)
        # cv2.drawContours(drawing,[cnt],0,(0,255,0),0)
        # cv2.drawContours(drawing,[hull],0,(0,0,255),0)

        # draw the circle
        cv2.circle(drawing, tuple(palmCenter), int(palmRadius), (0, 255, 0), 10)
        cv2.circle(drawing, tuple(palmCenter),
                       10, (255, 0, 0), -2)
        # hull = cv2.convexHull(cnt)


        # draw hand contour
        cv2.drawContours(drawing, [handContour], 0, (0, 255, 0), 1)
        # drawVertices(handContour, drawing)

        # = draw hull contour
        cv2.drawContours(drawing, [hullPoints], 0, (0, 0, 255), 2)
        drawVertices(hullPoints, drawing)


        # hull = cv2.convexHull(cnt,returnPoints = False)
        # # defects = cv2.convexityDefects(cnt,hull)
        # count_defects = 1 # was 0
        # cv2.drawContours(thresh1, contours, -1, (0,255,0), 3)
        # for i in range(defects.shape[0]):
        #     s, e, f, d = defects[i,0]
        #     start = tuple(cnt[s][0])
        #     end = tuple(cnt[e][0])
        #     far = tuple(cnt[f][0])
        #     a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
        #     b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
        #     c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
        #     # angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
        #     # if angle <= 100 and d > 6:
        #     #     count_defects += 1
        #     #     cv2.circle(crop_img,far,1,[0,0,255],-1)
        #     #dist = cv2.pointPolygonTest(cnt,far,True)
        #     cv2.line(crop_img,start,end,[0,255,0],2)
        #     #cv2.circle(crop_img,far,5,[0,0,255],-1)
        # if count_defects == 6:
        #     cv2.putText(img,"5 fingers", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        #     mouse.reset()
        # elif count_defects == 2: #assumes fist
        #     cv2.putText(img,"1 finger", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        #     if not hasattr(mouse, "init_x") or not mouse.init_x:
        #         mouse.init_x, mouse.init_y = mouse.get_pos()
        #     #mouse.scroll()
        # elif count_defects == 3:
        #     cv2.putText(img, "2 fingers", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        # elif count_defects == 4:
        #     #mouse.left_click()
        #     pass
        #     #cv2.putText(img,"3 fingers", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        # elif count_defects == 5:
        #     cv2.putText(img,"4 fingers", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        # else:
        #     cv2.putText(img,"PROJECT: Hand Mouse", (50,50),\
        #                 cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        cv2.imshow('drawing', drawing)
        #cv2.imshow('end', crop_img)

        cv2.imshow('Gesture', img)
        all_img = np.hstack((drawing, crop_img))

        # cv2.imshow('Contours', all_img)
        k = cv2.waitKey(10)
        if k == 27:
            break
    except:
        pass
