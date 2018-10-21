import cv2
import numpy as np


cam = cv2.VideoCapture(0)  # 打开内置摄像头，设置成1或者其他值来调用其他摄像头
if cam.isOpened() is False:  # 确认摄像头是否成功打开
    print('Error')
    exit(1)
while True:
    ret, frame = cam.read()
    cv2.imshow('frame', frame)  # 显示图像帧
    if cv2.waitKey(50) & 0xFF == ord('q'): # 每隔20ms采集一帧，按q键退出采集
        break
cam.release()
