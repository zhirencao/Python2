# 导入 OpenCV 库      "D:/1.png"
import cv2 as cv
# 导入 maplotlib
import matplotlib.pyplot as plt

# 加载 图像nage
img = cv.imread("D:/1.png")


# 截取部分图像
#cat = img[0:200, 0:200]
# 显示截取的图像
#cv.imshow("cat",cat)


# 颜色通道提取
#cur_img = img.copy()
# 注意参数的变化
#cur_img[:,:,0] = 0
#cur_img[:,:,1] = 0
#cv.imshow('R',cur_img)


# 颜色通道提取
#cur_img = img.copy()
#cur_img[:,:,0] = 0
#cur_img[:,:,2] = 0
#cv.imshow('G',cur_img)



# 等待时间，毫秒级，0 表示任意键终止
#cv.waitKey(0)
#cv.destroyAllWindows()


# 定义图片显示大小
top_size,buttom_size,left_size,right_size = (50,50,50,50)

# 复制法，也就是复制最边缘像素
replicate = cv.copyMakeBorder(img,top_size,buttom_size,left_size,right_size,borderType=cv.BORDER_REPLICATE)

# 反射法，对感兴趣的图像中的像素在两边进行复制例如：fedcbajabcdefghjhgfedcb
reflect = cv.copyMakeBorder(img,top_size,buttom_size,left_size,right_size,borderType=cv.BORDER_REFLECT)

# 反射法，也就是以最边缘像素为轴、对称、gfedcbjabcdefghigfedcba
reflect01 = cv.copyMakeBorder(img,top_size,buttom_size,left_size,right_size,borderType=cv.BORDER_REFLECT_101)

# 外包装法 cdeifghjabcdefghjabcdefg
wrap = cv.copyMakeBorder(img,top_size,buttom_size,left_size,right_size,borderType=cv.BORDER_WRAP)

# 常量法，常数值填充
constant = cv.copyMakeBorder(img,top_size,buttom_size,left_size,right_size,borderType=cv.BORDER_CONSTANT)

# 设置图像位置
plt.subplot(231)
# 设置图像显示
plt.imshow(img,'gray')
# 设置标题
plt.title('ORIGINAL')

plt.subplot(232)
plt.imshow(replicate,'gray')
plt.title("REPLICATE")

plt.subplot(233)
plt.imshow(reflect,'gray')
plt.title("REFLECT")

plt.subplot(234)
plt.imshow(reflect01,'gray')
plt.title("REPLICATE01")

plt.subplot(235)
plt.imshow(wrap,'gray')
plt.title("WRAP")

plt.subplot(236)
plt.imshow(constant,'gray')
plt.title("CONSTANT")

# 图像显示
plt.show()


# 融合的两张图像
img = cv.imread("./1.jpg")
img_cat = cv.imread("./2.jpg")
# 设置与 img 一样的数值
img_cat = cv.resize(img_cat,(721,300))

# 设置宽度值
res = cv.addWeighted(img,0.4,img_cat,0.6,0)

# 图像显示
plt.imshow(res)
plt.show()

# 需要使用 imwrite() 方法即可将图像保存起来
# 读取图像
img = cv.imread("./1.jpg",cv.IMREAD_GRAYSCALE)
# 图像保存
# 第一个参数是图像要保存的路径，第二个图像是要保存的图像
cv.imwrite("./demo.jpg",img)

