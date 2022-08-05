import cv2

video = cv2.VideoCapture("D:/2.mp4")

# 检查是否打开正确
if video.isOpened():
    # 我们都知道视频和游戏其实都是由图像组成的，通过访问图像的帧数连贯形成的，这里也是一样
    # video.read() 一帧一帧地读取
    # open 得到的是一个布尔值，就是 True 或者 False
    # frame 得到当前这一帧的图像
    open, frame = video.read()
else:
    open = False

while open:
    ret, frame = video.read()
    # 如果读到的帧数不为空，那么就继续读取，如果为空，就退出
    if frame is None:
        break
    if ret == True:
        # 转换为灰度图
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #cv2.imshow("video",gray)
        cv2.imshow("video",frame)
        # 这里使用 waitKey 可以控制视频的播放速度，数值越小，播放速度越快
        # 这里等于 27 也即是说按下 ESC 键即可退出该窗口
        if cv2.waitKey(10) & 0xFF == 27:
            break
video.release()
cv2.destroyAllWindows()