import cv2
import FaceRecognition as fr


def run():
    cam = cv2.VideoCapture(0)  # 打开内置摄像头，设置成1或者其他值来调用其他摄像头
    if cam.isOpened() is False:  # 确认摄像头是否成功打开
        print('Error,could not open the camera!')
        exit(1)
    while True:
        ret, frame = cam.read()
        fr.face_recognition(frame)
        if cv2.waitKey(50) & 0xFF == ord('q'): # 每隔20ms采集一帧，按q键退出采集
            break
    cam.release()    # 关闭摄像头


run()

