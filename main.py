
import cv2


def face_rec():
    # 加载视频
    cameraCapture = cv2.VideoCapture('D:/3.mp4')
    # cv2级联分类器CascadeClassifier,xml文件为训练数据
    face_cascade = cv2.CascadeClassifier('D:/Program Files/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
    # 读取数据
    success, frame = cameraCapture.read()
    while success and cv2.waitKey(1) == -1:
        # 读取数据
        ret, img = cameraCapture.read()
        # 进行人脸检测
        faces = face_cascade.detectMultiScale(img, 1.3, 5)
        # 绘制矩形框
        for (x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # 设置显示窗口
        cv2.namedWindow('camera', 0)
        cv2.resizeWindow('camera', 480, 640)
        # 显示处理后的视频
        cv2.imshow('camera', img)
        # 读取数据
        success, frame = cameraCapture.read()
    # 释放视频
    cameraCapture.release()
    # 释放所有窗口
    cv2.destroyAllWindows()


if __name__ == '__main__':
    face_rec()