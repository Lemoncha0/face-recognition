import cv2


def face_recognition(image):
    """处理图片，将图中的人脸框出"""
    # 获取训练好的人脸的参数数据，这里直接从GitHub上使用默认值
    face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface_default.xml')
    # 转化为灰度图片以加快处理速度
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 灰度图片
    # 探测图片中的人脸
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.15,  # 1.0475
        minNeighbors=5,
        minSize=(5, 5),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    print("发现{}个人脸!".format(len(faces)))
    if len(faces) > 0:
        for (x, y, w, h) in faces:
            # cv2.rectangle(image, (x, y), (x+w, y+w), (0, 255, 0), 2)    # 用矩形将人脸框出
            cv2.circle(image, ((x + x + w) // 2, (y + y + h) // 2), w // 2, (0, 255, 0), 2)
    cv2.imshow("Find Faces!", image)