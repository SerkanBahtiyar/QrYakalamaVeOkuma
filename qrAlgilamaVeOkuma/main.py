#quickResponse

import cv2 as cv
import numpy as np

path="venv/images/"
src=cv.imread(path+"qr.png")

gray=cv.cvtColor(src,cv.COLOR_BGR2GRAY)

qrcoder=cv.QRCodeDetector()

codeinfo, points, straight_qrcode=qrcoder.detectAndDecode(gray)
print(points)

result=np.copy(src)

cv.drawContours(result, [np.int32(points)], 0, (0,0,255), 2)

print("qr bilgisi: \n%s"% codeinfo)

cv.imshow("sonuc",result)
cv.waitKey()
