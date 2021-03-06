import cv2
import numpy as np


def contrast_demo(img1, c, b):  # 亮度就是每个像素所有通道都加上b
    rows, cols, channel = img1.shape
    blank = np.zeros([rows, cols, channel], img1.dtype)  # np.zeros(img1.shape, dtype=uint8)
    dst = cv2.addWeighted(img1, c, blank, 0, b)
    cv2.imshow("con_bri_demo", dst)


img1 = cv2.imread("E:\\contest\\CVPR_UG2_Challenge\\DarkFace_Train_2021\\image\\4.png", cv2.IMREAD_COLOR)


contrast_demo(img1, 13, 15)
cv2.waitKey(0)

cv2.destroyAllWindows()

