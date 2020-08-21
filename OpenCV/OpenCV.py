from cv2 import *

image = cv2.imread('startpic.png', 1)
cv2.imshow('Original', image)
blur = cv2.blur(image.copy(), (3, 3))
cv2.imshow("blur", blur)
cvtColor = cv2.cvtColor(blur.copy(), cv2.COLOR_BGR2GRAY)
cv2.imshow("cvtColor", cvtColor)
_, threshold = cv2.threshold(cvtColor.copy(), 70, 255, cv2.THRESH_BINARY)
cv2.imshow('Threshold', threshold)
adaptiveThreshold = cv2.adaptiveThreshold(cvtColor.copy(), 250, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 1)
cv2.imshow('AdaptiveThreshold', adaptiveThreshold)
contours, hierarchy = cv2.findContours(threshold.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours_img = threshold.copy()
cv2.drawContours(contours_img, contours, -1, (0, 255, 0), 5)
cv2.imshow("Segmentaition", contours_img)
template = cv2.imread("image.png", 1)
w, h, _ = template.shape
res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
bottom_right = (max_loc[0] + w, max_loc[1] + h)
cv2.rectangle(image, max_loc, bottom_right, 100, 2)
cv2.imshow("Template", template)
cv2.imshow("Matching", image)

# ждём нажатия клавиши
cv2.waitKey(0)

cv2.destroyAllWindows()
